

import csv


def is_missing(value):
    """Check whether a value represents missing data."""
    return (value or "").strip().lower() in {
        "", "na", "n/a", "null", "none"
    }


def clean_number(value):
    """Convert numeric text to a number, handling commas and missing values."""
    if is_missing(value):
        return None

    try:
        return float(value.replace(",", "").strip())
    except (ValueError, AttributeError):
        return None


def inspect_data(file_path):
    """Read a CSV, inspect its contents, and return a summary."""

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        columns = reader.fieldnames

    print("\n===== CSV DATA INSPECTION =====")
    print("Column names:", columns)
    print("Total rows:", len(rows))

    if rows:
        print("First row:", rows[0])

        if "ward" in rows[0]:
            print("First ward:", rows[0]["ward"])

        if "area_km2" in rows[0]:
            print("First ward area:", rows[0]["area_km2"])
    else:
        print("The CSV contains no data rows.")

    # Count missing values in each column
    print("\n===== MISSING VALUES =====")
    missing_values = {}

    for column in columns or []:
        missing = sum(
            1 for row in rows
            if is_missing(row.get(column))
        )
        missing_values[column] = missing
        print(f"{column}: {missing}")

    # Clean and summarise the area column
    print("\n===== AREA SUMMARY =====")

    if "area_km2" in (columns or []):
        areas = [
            clean_number(row.get("area_km2"))
            for row in rows
        ]

        valid_areas = [
            area for area in areas
            if area is not None
        ]

        if valid_areas:
            print("Valid area values:", len(valid_areas))
            print("Total area (km²):", round(sum(valid_areas), 4))
            print(
                "Average area (km²):",
                round(sum(valid_areas) / len(valid_areas), 4)
            )
        else:
            print("No valid area values found.")
    else:
        print("The CSV has no area_km2 column.")

    # Return the results so other code can reuse them
    summary = {
        "columns": columns,
        "total_rows": len(rows),
        "missing_values": missing_values,
    }

    return summary


def test_print():
    print("Hello from print")


def test_return():
    return "Hello from return"


if __name__ == "__main__":
    # Inspect the real Month 1 dataset
    result = inspect_data("wards.csv")

    print("\n===== RETURNED SUMMARY =====")
    print(result)

    # Demonstrate print versus return
    print("\n===== PRINT VERSUS RETURN =====")

    result1 = test_print()
    print("Result from test_print:", result1)

    result2 = test_return()
    print("Result from test_return:", result2)

    # Demonstrate number cleaning
    print("\n===== NUMBER CLEANING TESTS =====")
    print('"12,500" becomes:', clean_number("12,500"))
    print('"35,200" becomes:', clean_number("35,200"))
    print('"NA" becomes:', clean_number("NA"))
    print('An empty value becomes:', clean_number(""))
