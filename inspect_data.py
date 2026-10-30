import csv
from collections import Counter
from pathlib import Path

FILENAME = "healthcare_facilities.csv"
COLUMNS = ["fclass", "name"]

# Look for the CSV next to this script, then one folder up
here = Path(__file__).resolve().parent
for folder in (here, here.parent):
    path = folder / FILENAME
    if path.exists():
        break
else:
    raise FileNotFoundError(f"Could not find {FILENAME}")


def summarise(rows, column):
    values = [row[column].strip() for row in rows]
    filled = [v for v in values if v != ""]
    counts = Counter(filled)
    return {
        "column": column,
        "total_rows": len(values),
        "missing": len(values) - len(filled),
        "unique_values": len(counts),
        "top_3": counts.most_common(3),
    }


with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(f"File: {path.name}")
print(f"Rows: {len(rows)}")
print(f"Columns: {list(rows[0].keys())}")
print()

for col in COLUMNS:
    print(summarise(rows, col))
    print()

