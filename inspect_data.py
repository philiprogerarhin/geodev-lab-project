import csv
import sys
from collections import Counter

NA_VALUES = {"", "na", "n/a", "nan", "null", "none", "-"}
MAX_CATEGORIES = 15  # columns with this many distinct values or fewer get a counts table


def is_empty(value):
    """True for empty cells and NA-style values."""
    return value is None or value.strip().lower() in NA_VALUES


def clean_number(value):
    """Turn a messy cell like '1,234.5' into a float.
    Returns None for empty/NA cells or text that isn't a number."""
    if is_empty(value):
        return None
    text = value.strip().replace(",", "")  # thousands separators
    try:
        return float(text)
    except ValueError:
        return None


def summarise_column(values):
    """Return a stats dictionary for one column's list of raw cell values."""
    total = len(values)
    non_empty = [v.strip() for v in values if not is_empty(v)]
    empty = total - len(non_empty)
    unique = len(set(non_empty))

    stats = {
        "empty_or_na": empty,
        "pct_empty": round(100 * empty / total, 1) if total else 0.0,
        "unique_values": unique,
    }

    numbers = [n for n in (clean_number(v) for v in non_empty) if n is not None]
    looks_numeric = len(non_empty) > 0 and len(numbers) >= 0.8 * len(non_empty)

    if not non_empty:
        stats["type"] = "empty"
    elif unique == 1:
        stats["type"] = "constant"  # same value on every row, tells you nothing
        stats["value"] = non_empty[0]
    elif unique == len(non_empty) and looks_numeric:
        stats["type"] = "identifier"  # every value different: an ID, so no mean
    elif looks_numeric and unique <= MAX_CATEGORIES:
        stats["type"] = "category (numeric code)"
        stats["counts"] = Counter(non_empty).most_common()
    elif looks_numeric:
        stats["type"] = "numeric"
        stats["min"] = min(numbers)
        stats["max"] = max(numbers)
        stats["mean"] = sum(numbers) / len(numbers)
    else:
        stats["type"] = "text"
        if unique <= MAX_CATEGORIES:
            stats["counts"] = Counter(non_empty).most_common()
    return stats


def inspect_data(path):
    """Read a CSV and RETURN a summary dictionary (not just print it)."""
    # utf-8-sig strips the invisible BOM that Excel adds to the first header
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        rows = list(reader)

    summary = {
        "file": path,
        "row_count": len(rows),
        "columns": columns,
        "column_stats": {},
    }
    for col in columns:
        summary["column_stats"][col] = summarise_column([row[col] for row in rows])

    return summary  # without this line the caller gets None


def print_summary(summary):
    print(f"File: {summary['file']}")
    print(f"Rows: {summary['row_count']}")
    print(f"Columns: {', '.join(summary['columns'])}\n")
    for col, s in summary["column_stats"].items():
        print(f"- {col} [{s['type']}]  empty/NA: {s['empty_or_na']} ({s['pct_empty']}%)")
        if s["type"] == "numeric":
            print(f"    min={s['min']:g}  max={s['max']:g}  mean={s['mean']:.2f}")
        elif s["type"] == "constant":
            print(f"    every row is '{s['value']}': consider dropping this column")
        elif s["type"] == "identifier":
            print(f"    {s['unique_values']} unique values (ID column, no statistics)")
        elif "counts" in s:
            for value, n in s["counts"]:
                print(f"    {value}: {n}")
        elif s["type"] == "text":
            print(f"    {s['unique_values']} unique values")


if __name__ == "__main__":
    CSV_PATH = "healthcare_facilities.csv"  # the CSV in your Week 8 folder
    path = sys.argv[1] if len(sys.argv) > 1 else CSV_PATH
    result = inspect_data(path)
    print_summary(result)
