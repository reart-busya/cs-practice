def parse_event(line: str) -> dict:

    parts = line.split(None, 2)
    ValueGood = ["DEBUG", "INFO", "WARNING", "ERROR"]

    if len(parts) != 3:
        raise ValueError("Негодная строка")

    time = parts[0].strip()
    level = parts[1].strip()
    message = parts[2].strip()

    if level not in ValueGood:
        raise ValueError("Негодная строка")

    if message == "":
        raise ValueError("Негодная строка")

    return {
        "time": time,
        "level": level,
        "message": message
    }

def count_levels(lines: list[str]) -> dict:

    counts = {}

    for line in lines:

        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1

    return counts

def top_errors(lines: list[str], n):

    errors = {}

    for line in lines:

        try:
            event = parse_event(line)
            level = event["level"]
            message = event["message"]

            if level == "ERROR":
                errors[message] = errors.get(message, 0) + 1
        except ValueError:
            pass

    pairs = list(errors.items())
    sort_pairs = sorted(pairs, key = lambda pair: (-pair[1], pair[0]))

    result = []
    for pair in sort_pairs[:n]:
        result.append(list(pair))

    return result

def format_report(counts: dict, errors: list[list[str | int]]):

    report = "Отчёт по журналу\n\n"

    for level in sorted(counts):
        report += f"{level}: {counts[level]}\n"

    report += "\nЧастые ошибки:\n"

    for error in errors:
        report += f"- {error[0]} — {error[1]}\n"

    return report