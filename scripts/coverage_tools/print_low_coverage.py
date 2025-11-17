import xml.etree.ElementTree as ET
from pathlib import Path


def main(xml_path: str, top: int = 20) -> None:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    classes = root.findall(".//class")
    rows = [(c.get("filename"), float(c.get("line-rate")) * 100) for c in classes]
    rows.sort(key=lambda x: x[1])
    for i, r in enumerate(rows[:top], 1):
        print(f"{i:2}. {r[0]}: {r[1]:.2f}%")


if __name__ == "__main__":
    xml = Path(".tmp-results/reports/coverage_batch1.xml")
    if not xml.exists():
        print("Coverage XML not found:", xml)
    else:
        main(str(xml), top=30)
