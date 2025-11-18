from __future__ import annotations

import json
import math
import os
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import cast

TOKEN_RE = re.compile(r"[A-Za-zÄÖÜäöü0-9_]+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    s = text.lower()
    return [t for t in TOKEN_RE.findall(s) if len(t) > 1]


@dataclass
class Chunk:
    id: int
    source: str
    content: str
    tf: dict[str, int]


@dataclass
class TfIdfIndex:
    chunks: list[Chunk]
    df: dict[str, int]
    n_docs: int

    def to_dict(self) -> dict[str, object]:
        return {
            "n_docs": self.n_docs,
            "df": self.df,
            "chunks": [
                {"id": c.id, "source": c.source, "content": c.content, "tf": c.tf}
                for c in self.chunks
            ],
        }

    @staticmethod
    def from_dict(d: dict[str, object]) -> TfIdfIndex:
        chunks_raw: list[dict[str, object]] = []
        cr: object = d.get("chunks", [])
        if isinstance(cr, list):
            for item in cast(list[object], cr):
                if isinstance(item, dict):
                    item_typed: dict[str, object] = {}
                    for kk, vv in cast(dict[object, object], item).items():
                        item_typed[str(kk)] = vv
                    chunks_raw.append(item_typed)

        chunks: list[Chunk] = []
        for cd in chunks_raw:
            cid_default = len(chunks)
            cid_obj: object = cd.get("id", cid_default)
            if isinstance(cid_obj, int | float | str):
                try:
                    cid = int(cid_obj)
                except Exception:
                    cid = cid_default
            else:
                cid = cid_default

            src = str(cd.get("source", ""))
            content = str(cd.get("content", ""))
            tf: dict[str, int] = {}
            tf_any: object = cd.get("tf", {})
            if isinstance(tf_any, Mapping):
                for k_obj, v_obj in tf_any.items():
                    try:
                        k_s = str(k_obj)
                        v_i = int(v_obj)  # type: ignore[arg-type]
                    except Exception:
                        continue
                    tf[k_s] = v_i
            chunks.append(Chunk(id=cid, source=src, content=content, tf=tf))

        df: dict[str, int] = {}
        df_any: object = d.get("df", {})
        if isinstance(df_any, Mapping):
            for k_obj, v_obj in cast(Mapping[object, object], df_any).items():
                try:
                    k_s = str(k_obj)
                    v_i = int(v_obj)  # type: ignore[arg-type]
                except Exception:
                    continue
                df[k_s] = v_i

        n_docs_any: object = d.get("n_docs", 0)
        try:
            n_docs = int(n_docs_any)  # type: ignore[arg-type]
        except Exception:
            n_docs = 0

        return TfIdfIndex(chunks=chunks, df=df, n_docs=n_docs)


def _iter_files(paths: Iterable[str], exts: tuple[str, ...] = (".md", ".txt")) -> Iterable[Path]:
    for p in paths:
        pp = Path(p)
        if pp.is_file() and pp.suffix.lower() in exts:
            yield pp
        elif pp.is_dir():
            for child in pp.iterdir():
                if child.is_file() and child.suffix.lower() in exts:
                    yield child


def build_index(paths: list[str]) -> TfIdfIndex:
    chunks: list[Chunk] = []
    df: dict[str, int] = {}
    n_docs = 0

    for file in _iter_files(paths):
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        n_docs += 1
        # Baseline: eine Datei = ein Chunk (später: feiner chunking nach Abschnitten)
        toks = tokenize(text)
        tf: dict[str, int] = {}
        seen: set[str] = set()
        for t in toks:
            tf[t] = tf.get(t, 0) + 1
            if t not in seen:
                df[t] = df.get(t, 0) + 1
                seen.add(t)
        chunks.append(Chunk(id=len(chunks), source=str(file), content=text[:4000], tf=tf))

    return TfIdfIndex(chunks=chunks, df=df, n_docs=n_docs)


def save_index(index: TfIdfIndex, out_path: str) -> None:
    Path(os.path.dirname(out_path) or ".").mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        payload: dict[str, object] = index.to_dict()
        json.dump(payload, f, ensure_ascii=False)


def load_index(path: str) -> TfIdfIndex | None:
    try:
        with open(path, encoding="utf-8") as f:
            raw: dict[str, object] = cast(dict[str, object], json.load(f))
            return TfIdfIndex.from_dict(raw)
    except Exception:
        return None


def _cosine_sim(qw: dict[str, float], dw: dict[str, float]) -> float:
    dot = 0.0
    qn = 0.0
    dn = 0.0
    for k, v in qw.items():
        qn += v * v
        if k in dw:
            dot += v * dw[k]
    for v in dw.values():
        dn += v * v
    if qn == 0 or dn == 0:
        return 0.0
    return dot / (math.sqrt(qn) * math.sqrt(dn))


def retrieve(index: TfIdfIndex, query: str, top_k: int = 3) -> list[dict[str, str]]:
    """Gibt die Top-K Chunks als Liste von {source, content, score} zurück."""

    toks = tokenize(query)
    qtf: dict[str, int] = {}
    for t in toks:
        qtf[t] = qtf.get(t, 0) + 1

    # Gewichte berechnen (idf = log(1 + n/(df+1))) konservativ, robust bei n=0
    n = max(1, index.n_docs)
    idf: dict[str, float] = {}
    for t, df_val in index.df.items():
        idf[t] = math.log(1.0 + (n / float(df_val + 1)))

    qw: dict[str, float] = {t: float(tf) * idf.get(t, 0.0) for t, tf in qtf.items()}

    scored: list[tuple[float, Chunk]] = []
    for ch in index.chunks:
        dw = {t: float(tf) * idf.get(t, 0.0) for t, tf in ch.tf.items()}
        s = _cosine_sim(qw, dw)
        if s > 0:
            scored.append((s, ch))

    scored.sort(key=lambda x: x[0], reverse=True)
    out: list[dict[str, str]] = []
    for s, ch in scored[: max(1, top_k)]:
        out.append({"source": ch.source, "content": ch.content, "score": f"{s:.4f}"})
    return out
