import csv

CSV_FILE = "healthcare_facilities.csv"
NA_VALUES = {"", "na", "n/a", "nan", "null", "none", "-"}


def read_rows(path):
    """Read a CSV and return a list of row dictionaries."""
    # utf-8-sig removes the invisible BOM that Excel adds to the first header
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def clean_values(values):
    """Return the real values only: stripped, with empty and NA cells removed."""
    return [v.strip() for v in values if v is not None and v.strip().lower() not in NA_VALUES]


def summarise(values):
    """Return count, smallest, largest and average for one column.
    Columns that are not numbers get None for smallest, largest and average."""
    cleaned = clean_values(values)
    numbers = []
    for v in cleaned:
        try:
            numbers.append(float(v.replace(",", "")))  # removes thousands separators
        except ValueError:
            pass

    result = {"count": len(cleaned), "smallest": None, "largest": None, "average": None}
    if cleaned and len(numbers) == len(cleaned):  # every real value is a number
        result["smallest"] = min(numbers)
        result["largest"] = max(numbers)
        result["average"] = sum(numbers) / len(numbers)
    return result


def summarise_all(rows):
    """Summarise every column and RETURN a dictionary of results."""
    summary = {}
    for column in rows[0].keys():
        summary[column] = summarise([row[column] for row in rows])
    return summary


rows = read_rows(CSV_FILE)
results = summarise_all(rows)

for column, s in results.items():
    if s["average"] is None:
        print(f"{column}: count={s['count']}  (text column, no min/max/average)")
    else:
        print(f"{column}: count={s['count']}  smallest={s['smallest']:,.0f}  "
              f"largest={s['largest']:,.0f}  average={s['average']:,.2f}")