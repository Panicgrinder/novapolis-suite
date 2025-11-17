import xml.etree.ElementTree as ET
from pathlib import Path

xmlp = Path(".tmp-results/reports/coverage_batch1.xml")
if not xmlp.exists():
    print("coverage XML not found:", xmlp)
    raise SystemExit(1)

excludes = set(
    [
        "scripts/eval_loader.py",
        "scripts/check_openai_key.py",
        "scripts/fix_donelog_times.py",
        "scripts/generate_eval_dataset.py",
        "scripts/eval_ui.py",
        "novapolis_agent/scripts/run_eval.py",
        "scripts/openai_finetune.py",
        "utils/eval_utils.py",
        "app/api/chat.py",
        "utils/context_notes.py",
    ]
)

tree = ET.parse(str(xmlp))
root = tree.getroot()
files = []
for cls in root.findall(".//class"):
    fn = cls.get("filename")
    lr = cls.get("line-rate")
    try:
        lrf = float(lr)
    except Exception:
        continue
    if not fn:
        continue
    # normalize path separators and strip leading project/package prefixes
    fn_norm = fn.replace("\\", "/").lstrip("./")
    # If file is under 'novapolis_agent/' prefix in XML, remove that prefix to
    # allow matching excludes by suffix.
    if fn_norm.startswith("novapolis_agent/"):
        fn_norm = fn_norm[len("novapolis_agent/") :]
    # Ignore package __init__ files (low value for coverage bumps)
    if fn_norm.endswith("/__init__.py") or fn_norm == "__init__.py":
        continue
    # If any exclude equals the suffix, skip
    if any(fn_norm.endswith(ex) or fn_norm == ex for ex in excludes):
        continue
    files.append((fn_norm, lrf))

# sort by ascending coverage then by name
files_sorted = sorted(files, key=lambda x: (x[1], x[0]))

print("Top low-coverage candidates (next 20):")
for i, (f, r) in enumerate(files_sorted[:20], 1):
    print(f"{i:2d}. {f} -> {r*100:.1f}%")

# print a suggested batch of 10
suggested = [f for f, _ in files_sorted[:10]]
print("\nSuggested Batch (10 files):")
for s in suggested:
    print("-", s)
