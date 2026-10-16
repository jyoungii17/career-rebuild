import csv
from pathlib import Path

REQUIRED_COLUMNS = ("customer", "email", "order_total")

def load_rows(csv_path):
    with Path(csv_path).open(
        "r", newline="", encoding="utf-8-sig"
    ) as csv_file:
        reader = csv.DictReader(csv_file)

        if not reader.fieldnames:
            raise ValueError("The CSV is empty or has no header row.")

        missing = [
            column
            for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing:
            raise ValueError(
                f"Missing required column(s): {', '.join(missing)}"
            )

        return list(reader)
def clean_row(row):
    cleaned = {}

    for column in REQUIRED_COLUMNS:
        value = row.get(column) or ""
        cleaned[column] = value.strip()

    return cleaned
def validate_row(row):
    errors = []

    if not row["customer"]:
        errors.append("blank customer")

    if not row["email"]:
        errors.append("blank email")

    try:
        order_total = float(row["order_total"])
    except ValueError:
        errors.append("invalid total")
    else:
        if order_total < 0:
            errors.append("negative total")

    return errors
def is_duplicate(row, seen_rows):
    row_key = tuple(row[column] for column in REQUIRED_COLUMNS)

    if row_key in seen_rows:
        return True
    
    seen_rows.add(row_key)
    return False
def write_clean_rows(rows, output_path):
    with Path(output_path).open(
        "w", newline="", encoding="utf-8"
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=REQUIRED_COLUMNS,
        )
        writer.writeheader()
        writer.writerows(rows)
def write_report(report, output_path):
    lines = [
        "Cleaning Report",
        f"Input rows: {report['input rows']}",
        f"Kept rows: {report['kept rows']}",
        f"Rejected rows: {report['rejected rows']}",
        f"Duplicate rows: {report['duplicate rows']}",
        f"Blank customers: {report['blank customer']}",
        f"Blank emails: {report['blank email']}",
        f"Invalid totals: {report['invalid total']}",
        f"Negative totals: {report['negative total']}",
    ]

    with Path(output_path).open("w", encoding="utf-8") as report_file:
        report_file.write("\n".join(lines) + "\n")