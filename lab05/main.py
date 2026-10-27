from pathlib import Path
from logstats import count_levels, top_errors, format_report


def main():
    filename = input().strip()
    log_path = Path(filename)
    if not log_path.is_absolute():
        log_path = Path(__file__).parent / log_path

    with log_path.open("r", encoding="utf-8") as log:
        counts = count_levels(log)

    total_parsed = sum(
        count for level, count in counts.items()
        if level != "BROKEN"
    )

    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total_parsed)
    print(error_count)
    print(broken_count)

    with log_path.open("r", encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)

    report_path = Path(__file__).with_name("report.txt")
    report_path.write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()