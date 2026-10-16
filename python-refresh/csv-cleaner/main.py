from pathlib import Path

from cleaner import (
    clean_row,
    is_duplicate,
    load_rows,
    validate_row,
    write_clean_rows,
    write_report,
)


INPUT_FILE = Path(__file__).with_name("customer_orders_raw.csv")
OUTPUT_FILE = Path(__file__).with_name("customer_orders_clean.csv")
REPORT_FILE = Path(__file__).with_name("cleaning_report.txt")


def main():
    rows = load_rows(INPUT_FILE)
    cleaned_rows = [clean_row(row) for row in rows]
    valid_rows = []
    seen_rows = set()

    report = {
        "input rows": len(rows),
        "kept rows": 0,
        "rejected rows": 0,
        "duplicate rows": 0,
        "blank customer": 0,
        "blank email": 0,
        "invalid total": 0,
        "negative total": 0,
    }

    print(f"Loaded {len(rows)} rows.")

    for row in cleaned_rows:
        errors = validate_row(row)
        customer = row["customer"] or "<blank customer>"

        if errors:
            report["rejected rows"] += 1

            for error in errors:
                report[error] += 1

            print(f"{customer}: {', '.join(errors)}")
        elif is_duplicate(row, seen_rows):
            report["rejected rows"] += 1
            report["duplicate rows"] += 1
            print(f"{customer}: duplicate")
        else:
            valid_rows.append(row)
            report["kept rows"] += 1
            print(f"{customer}: valid")

    write_clean_rows(valid_rows, OUTPUT_FILE)
    write_report(report, REPORT_FILE)

    print(f"Wrote {len(valid_rows)} cleaned rows to {OUTPUT_FILE.name}")
    print(f"Wrote report to {REPORT_FILE.name}")


if __name__ == "__main__":
    main()