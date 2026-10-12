import sys
# Импортируем наши готовые функции из соседнего модуля 
from stats import average_by_city, read_valid, warmest_city

# 1. Читаем весь журнал из стандартного ввода до конца, как требует задание
lines = sys.stdin.read().splitlines()

# 2. Прогоняем сырые строки через нашу функцию фильтрации
valid_records = read_valid(lines)

# 3. Считаем, сколько записей успешно разобрано
valid_count = len(valid_records)

# 4. Считаем, сколько строк пропущено ИЗ-ЗА ОШИБОК.
non_empty_lines = [line for line in lines if line.strip()]
error_count = len(non_empty_lines) - valid_count

# 5. Находим самый теплый город и вытягиваем его среднюю температуру
if valid_records: # Проверяем, что есть хотя бы одна хорошая запись
    best_city = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    best_temp = averages[best_city]
else:
    best_temp = 0.0

# 6. Печатаем ровно три строки в нужном порядке:
print(valid_count)
print(error_count)
# Печатаем температуру (наша функция average_by_city уже округлила её до десятых)
print(best_temp)

# Азов;24.5;2026-07-01
# мусор
# Азов;25.5;2026-07-02
# Таганрог;30;2026-07-01
# 3
# 1
# 30.0