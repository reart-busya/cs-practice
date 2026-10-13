import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()

valid_records = read_valid(lines)

valid_count = len(valid_records)

non_empty_lines = [line for line in lines if line.strip()]
error_count = len(non_empty_lines) - valid_count

if valid_records:
    best_city = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    best_temp = averages[best_city]
else:
    best_temp = 0.0

print(valid_count)
print(error_count)
print(best_temp)

# Азов;24.5;2026-07-01
# мусор
# Азов;25.5;2026-07-02
# Таганрог;30;2026-07-01
# 3
# 1
# 30.0

