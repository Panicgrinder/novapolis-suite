from __future__ import annotations

import csv
import math
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATASETS_ROOT = PROJECT_ROOT / ".tmp" / "datasets"


def _datasets_root() -> Path:
    override = os.environ.get("EVAL_THIRD_PARTY_DATASETS_ROOT")
    if override:
        return Path(override)
    return DEFAULT_DATASETS_ROOT


def _normalize_token(token: str) -> str:
    t = token.strip().lower()
    t = t.replace("ae", "a").replace("oe", "o").replace("ue", "u")
    t = t.replace("ä", "a").replace("ö", "o").replace("ü", "u").replace("ß", "ss")
    t = re.sub(r"[^a-z0-9\-\s]", "", t)
    return t.strip()


def _tokenize(text: str) -> list[str]:
    cleaned = _normalize_token(text)
    return [tok for tok in re.split(r"\s+", cleaned) if tok]


def _iter_candidate_paths(rel_paths: list[str]) -> list[Path]:
    root = _datasets_root()
    out: list[Path] = []
    for rel in rel_paths:
        path = root / rel
        if path.exists() and path.is_file():
            out.append(path)
    return out


@lru_cache(maxsize=1)
def load_openthesaurus_index() -> dict[str, list[str]]:
    rel = ["OpenThesaurus-Textversion/openthesaurus.txt"]
    paths = _iter_candidate_paths(rel)
    if not paths:
        return {}

    max_lines = int(os.environ.get("EVAL_OPENTHESAURUS_MAX_LINES", "250000"))
    index: dict[str, list[str]] = {}

    def _clean_term(raw: str) -> str:
        t = raw.strip()
        t = re.sub(r"\s*\([^)]*\)", "", t)
        t = t.replace("...", " ")
        return _normalize_token(t)

    line_no = 0
    with paths[0].open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            line_no += 1
            if line_no > max_lines:
                break
            if not line or line.startswith("#"):
                continue
            parts_raw = [p for p in line.strip().split(";") if p.strip()]
            parts = [_clean_term(p) for p in parts_raw]
            parts = [p for p in parts if p]
            if len(parts) < 2:
                continue

            for term in parts:
                acc = index.setdefault(term, [])
                for other in parts:
                    if other == term:
                        continue
                    if other not in acc:
                        acc.append(other)

    return index


def lookup_openthesaurus_synonyms(term: str, cap: int = 12) -> list[str]:
    key = _normalize_token(term)
    if not key:
        return []
    values = load_openthesaurus_index().get(key, [])
    return values[:cap]


@lru_cache(maxsize=1)
def load_sts_idf() -> dict[str, float]:
    rel_paths = [
        "german-STSbenchmark-master/german-STSbenchmark-master/data/deepl/stsb_de_train.csv",
        "german-STSbenchmark-master/german-STSbenchmark-master/data/aws/stsb_de_train.csv",
    ]
    paths = _iter_candidate_paths(rel_paths)
    if not paths:
        return {}

    df: dict[str, int] = {}
    docs = 0

    for path in paths:
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            reader = csv.reader(handle, delimiter="\t")
            for row in reader:
                if len(row) < 3:
                    continue
                s1 = row[1]
                s2 = row[2]
                for sent in (s1, s2):
                    toks = set(_tokenize(sent))
                    if not toks:
                        continue
                    docs += 1
                    for tok in toks:
                        df[tok] = df.get(tok, 0) + 1

    if docs == 0:
        return {}

    idf: dict[str, float] = {}
    for tok, freq in df.items():
        idf[tok] = math.log((docs + 1) / (freq + 1)) + 1.0
    return idf


def sts_relevance_score(prompt: str, response: str) -> float:
    p = set(_tokenize(prompt))
    r = set(_tokenize(response))
    if not p or not r:
        return 0.0

    idf = load_sts_idf()

    def _w(tok: str) -> float:
        return idf.get(tok, 1.0)

    inter = p & r
    p_sum = sum(_w(t) for t in p)
    inter_sum = sum(_w(t) for t in inter)
    if p_sum <= 0:
        return 0.0
    return max(0.0, min(1.0, inter_sum / p_sum))


@lru_cache(maxsize=1)
def load_compound_resources() -> dict[str, Any]:
    root = (
        _datasets_root()
        / "jwordsplitter-master"
        / "jwordsplitter-master"
        / "src"
        / "main"
        / "resources"
        / "de"
        / "danielnaber"
        / "jwordsplitter"
    )

    lexicon_path = root / "languagetool-dict.txt"
    prefixes_path = root / "germanPrefixes.txt"
    exceptions_path = root / "exceptionsGerman.txt"

    lexicon: set[str] = set()
    prefixes: list[str] = []
    exceptions: dict[str, list[str]] = {}

    if lexicon_path.exists():
        with lexicon_path.open("r", encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                if not line or line.startswith("#"):
                    continue
                tok = _normalize_token(line)
                if tok:
                    lexicon.add(tok)

    if prefixes_path.exists():
        with prefixes_path.open("r", encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                tok = _normalize_token(line)
                if tok:
                    prefixes.append(tok)

    if exceptions_path.exists():
        with exceptions_path.open("r", encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                raw = line.strip()
                if not raw or raw.startswith("#") or "|" not in raw:
                    continue
                pieces = [_normalize_token(p) for p in raw.split("|")]
                pieces = [p for p in pieces if p]
                if len(pieces) >= 2:
                    merged = "".join(pieces)
                    exceptions[merged] = pieces

    prefixes.sort(key=len, reverse=True)
    return {"lexicon": lexicon, "prefixes": prefixes, "exceptions": exceptions}


@lru_cache(maxsize=1)
def load_pos_lemma_map() -> dict[str, set[str]]:
    base = (
        _datasets_root()
        / "german-pos-dict-master"
        / "german-pos-dict-master"
        / "src"
        / "main"
        / "resources"
        / "org"
        / "languagetool"
        / "resource"
        / "de"
    )
    paths = [base / "sonstige.txt", base / "EIG.txt"]

    mapping: dict[str, set[str]] = {}
    max_lines = int(os.environ.get("EVAL_POS_MAX_LINES", "400000"))
    read_lines = 0

    for path in paths:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8", errors="ignore") as handle:
            for line in handle:
                if read_lines >= max_lines:
                    return mapping
                read_lines += 1

                raw = line.strip()
                if not raw or raw.startswith("#"):
                    continue

                cols = raw.split("\t")
                if len(cols) < 2:
                    continue

                surface = _normalize_token(cols[0])
                lemma = _normalize_token(cols[1])
                if not surface:
                    continue
                acc = mapping.setdefault(surface, set())
                if lemma:
                    acc.add(lemma)

    return mapping


def split_compound_token(token: str) -> list[str]:
    tok = _normalize_token(token)
    if len(tok) < 7:
        return []

    resources = load_compound_resources()
    lexicon = resources["lexicon"]
    prefixes = resources["prefixes"]
    exceptions = resources["exceptions"]

    if tok in exceptions:
        return exceptions[tok]

    for prefix in prefixes:
        if not tok.startswith(prefix):
            continue
        rest = tok[len(prefix) :]
        if len(rest) < 3:
            continue
        candidates = [rest]
        if rest.startswith("s") and len(rest) > 3:
            candidates.append(rest[1:])
        for cand in candidates:
            if cand in lexicon:
                return [prefix, cand]

    return []


def expand_tokens_for_term_search(text: str) -> set[str]:
    tokens = set(_tokenize(text))
    expanded = set(tokens)

    pos_map = load_pos_lemma_map()
    for tok in list(tokens):
        lemmas = pos_map.get(tok)
        if lemmas:
            expanded.update(lemmas)

        parts = split_compound_token(tok)
        if parts:
            expanded.update(parts)

    return expanded


def validate_german_terms(terms: list[str]) -> dict[str, Any]:
    pos_map = load_pos_lemma_map()
    resources = load_compound_resources()
    lexicon = resources["lexicon"]

    unknown: list[str] = []
    details: dict[str, str] = {}

    for term in terms:
        key = _normalize_token(term)
        if not key:
            continue

        if " " in key:
            parts = [p for p in key.split(" ") if p]
            unknown_parts = [p for p in parts if p not in pos_map and p not in lexicon]
            if unknown_parts:
                unknown.append(term)
                details[term] = "unknown_parts:" + ",".join(unknown_parts)
            continue

        if key in pos_map or key in lexicon:
            continue

        split = split_compound_token(key)
        if split:
            continue

        unknown.append(term)
        details[term] = "not_in_pos_or_splitter"

    return {
        "unknown_terms": unknown,
        "unknown_count": len(unknown),
        "details": details,
    }


@lru_cache(maxsize=1)
def load_languagetool_confusion_pairs() -> list[tuple[str, str]]:
    path = (
        _datasets_root()
        / "LanguageTool-stable"
        / "LanguageTool-6.6"
        / "org"
        / "languagetool"
        / "resource"
        / "de"
        / "confusion_sets.txt"
    )
    if not path.exists():
        return []

    out: list[tuple[str, str]] = []
    max_lines = int(os.environ.get("EVAL_LT_CONFUSION_MAX_LINES", "200000"))
    line_no = 0

    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            line_no += 1
            if line_no > max_lines:
                break
            raw = line.strip()
            if not raw or raw.startswith("#") or "->" not in raw:
                continue

            left_part = raw.split(";", 1)[0]
            side = left_part.split("->")
            if len(side) != 2:
                continue
            wrong = _normalize_token(side[0])
            right = _normalize_token(side[1])
            if wrong and right:
                out.append((wrong, right))

    return out


def languagetool_quality_issues(text: str) -> dict[str, Any]:
    normalized = _normalize_token(text)
    tokens = set(_tokenize(normalized))

    confusion_hits: list[str] = []
    for wrong, right in load_languagetool_confusion_pairs():
        if wrong in tokens and right not in tokens:
            confusion_hits.append(f"{wrong}->{right}")

    spacing_issues = 0
    if "  " in text:
        spacing_issues += 1
    if re.search(r"\s+[\.,;:!?]", text):
        spacing_issues += 1

    issue_count = len(confusion_hits) + spacing_issues
    # Score 1.0 means no obvious issues.
    score = max(0.0, 1.0 - min(issue_count, 8) / 8.0)

    return {
        "score": score,
        "issue_count": issue_count,
        "confusion_hits": confusion_hits[:10],
        "spacing_issues": spacing_issues,
    }
