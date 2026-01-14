"""Extract conflict list + FACT? list from curated review markdown.

This script is intentionally heuristic: curated review files are free-form.
We extract:
- Top N conflicts from bullets tagged [OPEN]
- All FACT? bullets

Output: a markdown report under `.tmp/results/reports/`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

RE_FACT = re.compile(r"^\s*-\s*\[FACT\?\]\s*(.+?)\s*$")
RE_OPEN = re.compile(r"^\s*-\s*\[OPEN\]\s*(.+?)\s*$")


@dataclass(frozen=True)
class Finding:
    kind: str  # "OPEN" | "FACT?"
    text: str
    source_file: str
    line_no: int


def repo_root() -> Path:
    # scripts/ is at repo root
    return Path(__file__).resolve().parents[1]


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def iter_findings(md_path: Path) -> Iterable[Finding]:
    lines = read_lines(md_path)
    rel = str(md_path.as_posix())

    for idx, line in enumerate(lines, start=1):
        m = RE_OPEN.match(line)
        if m:
            yield Finding(kind="OPEN", text=m.group(1).strip(), source_file=rel, line_no=idx)
            continue

        m = RE_FACT.match(line)
        if m:
            yield Finding(kind="FACT?", text=m.group(1).strip(), source_file=rel, line_no=idx)


def classify_layer(text: str) -> str:
    """Heuristic mapping for Core/Reference/Narrative."""
    t = text.lower()

    # Narrative / scenes
    if "[scene]" in t or "szene" in t or "scene" in t:
        return "Narrative"

    # Reference objects
    if any(
        k in t
        for k in [
            "inventar",
            "projekt",
            "logistik",
            "missionslog",
            "relationslog",
            "index",
            "canvas",
        ]
    ):
        return "Reference"

    # Core-ish conflicts
    if any(
        k in t
        for k in [
            "n7",
            "e2",
            "e3",
            "gasunfall",
            "tunnel",
            "fraktion",
            "hauptfraktion",
            "c6",
            "d5",
            "linie",
            "abzweig",
        ]
    ):
        return "Core"

    return "Reference"


def suggest_ssot_files(text: str) -> list[str]:
    """Very conservative: only suggest a few well-known anchors based on keywords."""
    t = text.lower()
    out: list[str] = []

    def add(p: str) -> None:
        if p not in out:
            out.append(p)

    # Admin / core anchors
    if any(
        k in t
        for k in ["n7", "e2", "e3", "tunnel", "fortschritt", "fraktion", "hauptfraktion", "wissen"]
    ):
        add("novapolis-rp/database-rp/00-admin/memory-bundle.md")
        add("novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md")

    if any(k in t for k in ["missionslog", "mission"]):
        add("novapolis-rp/database-rp/00-admin/Missionslog.md")

    if any(k in t for k in ["logistik", "transfer", "fracht"]):
        add("novapolis-rp/database-rp/00-admin/Logistik.md")

    if any(k in t for k in ["timeline", "t+0"]):
        add("novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md")

    if any(k in t for k in ["inventar"]):
        add("novapolis-rp/database-rp/04-inventory/Novapolis-inventar.md")

    return out


def unique_by_text(items: Sequence[Finding]) -> list[Finding]:
    seen = set()
    out: list[Finding] = []
    for f in items:
        key = re.sub(r"\s+", " ", f.text.strip()).lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(f)
    return out


def write_report(
    *,
    out_path: Path,
    sources: Sequence[Path],
    opens: Sequence[Finding],
    facts: Sequence[Finding],
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    def md_link(file: str, line_no: int) -> str:
        # Render as workspace-relative path (slash) + line anchor for VS Code linkification.
        # We keep it plain markdown here; VS Code will resolve relative.
        file_norm = file.replace("\\", "/")
        return f"[{file_norm}#L{line_no}]({file_norm}#L{line_no})"

    lines: list[str] = []
    ts = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines += [
        "---",
        f"stand: {ts}",
        "update: Curated Review-Extrakt (Konflikte + FACT?).",
        "checks: scripts/extract_curated_conflicts.py RUN",
        "---",
        "",
        "Curated Konfliktliste + FACT?-Liste",
        "===============================",
        "",
        "Quellen",
        "-------",
    ]

    for p in sources:
        rel = p.as_posix()
        lines.append(f"- {rel}")

    lines += [
        "",
        "Top 10 Konflikte (aus [OPEN])",
        "-----------------------------",
        "",
    ]

    top = list(unique_by_text(opens))[:10]
    if not top:
        lines.append("- (keine [OPEN]-Einträge gefunden)")
    else:
        for i, f in enumerate(top, start=1):
            layer = classify_layer(f.text)
            ssot = suggest_ssot_files(f.text)
            lines.append(f"{i}. {f.text}")
            lines.append(f"   - Layer: {layer}")
            lines.append(f"   - Quelle: {md_link(f.source_file, f.line_no)}")
            if ssot:
                lines.append("   - Betroffene SSOT-Dateien (vermutet):")
                for p in ssot:
                    lines.append(f"     - {p}")
            else:
                lines.append("   - Betroffene SSOT-Dateien (vermutet): (noch zuzuordnen)")

    lines += [
        "",
        "FACT?-Liste (aus [FACT?])",
        "-------------------------",
        "",
    ]

    facts_u = unique_by_text(facts)
    if not facts_u:
        lines.append("- (keine [FACT?]-Einträge gefunden)")
    else:
        for f in facts_u:
            layer = classify_layer(f.text)
            lines.append(f"- {f.text}")
            lines.append(f"  - Layer (Heuristik): {layer}")
            lines.append(f"  - Quelle: {md_link(f.source_file, f.line_no)}")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--reviews",
        nargs="*",
        default=None,
        help=(
            "Review markdown files (defaults to "
            "novapolis-rp/database-curated/staging/*.review.md)"
        ),
    )
    p.add_argument(
        "--out",
        default=None,
        help=(
            "Output path (defaults to "
            ".tmp/results/reports/curated_conflicts_postflight_YYYYMMDD_HHMM.md)"
        ),
    )
    return p.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = repo_root()

    if args.reviews:
        review_paths = [Path(p) if Path(p).is_absolute() else (root / p) for p in args.reviews]
    else:
        review_paths = sorted(
            (root / "novapolis-rp" / "database-curated" / "staging").glob("*.review.md")
        )

    review_paths = [p for p in review_paths if p.exists()]
    if not review_paths:
        raise SystemExit("No review files found.")

    findings: list[Finding] = []
    for p in review_paths:
        findings.extend(list(iter_findings(p)))

    opens = [f for f in findings if f.kind == "OPEN"]
    facts = [f for f in findings if f.kind == "FACT?"]

    if args.out:
        out_path = Path(args.out) if Path(args.out).is_absolute() else (root / args.out)
    else:
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
        out_path = (
            root / ".tmp" / "results" / "reports" / f"curated_conflicts_postflight_{stamp}.md"
        )

    write_report(out_path=out_path, sources=review_paths, opens=opens, facts=facts)
    print(str(out_path.as_posix()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
