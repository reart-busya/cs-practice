def parse_record(line: str) -> dict:
    """Разбирает строку ввода в словарь. Вызывает ValueError, если строка негодная"""
    
    parts = line.split(";") # Разделяем строку по символу ";"
    
    # Проверка 1: полей должно быть ровно три (город, температура, дата)
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно три поля, разделенных \";\" ")
    
    # Распаковываем полученные части в переменные
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    # Проверка 2: город или дата не должны быть пустыми
    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")
    
    # Проверка 3: температура должна быть числом
    try:
        temp = float(temp_str)
    except ValueError:
        # Перехватываем ошибку float и вызываем свою с понятным сообщением
        raise ValueError(f"Температура не является числом: '{temp_str}'")
    
    # Если все проверки пройдены, возвращаем словарь
    return {
        "city": city,
        "temp": temp,
        "date": date
    }

def read_valid(lines: list[str]) -> list[dict]:
    """Разбирает строки журнала, пропуская пустые и негодные."""
    
    valid_records = []  # Создаем пустой список для хранения хороших записей
    
    for line in lines:
        if not line.strip(): # Убираем пробелы по краям. Если строка после этого пустая, пропускаем её молча
            continue
            
        try:
            # Пытаемся разобрать строку нашей первой функцией
            record = parse_record(line)
            # Если ошибок не возникло, добавляем полученный словарь в итоговый список
            valid_records.append(record)
        except ValueError:
            # Если parse_record выбросила ошибку, мы её ловим здесь
            # И просто переходим к следующей строке (пропускаем негодную)
            continue
            
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    """Средняя температура по каждому городу, округлённая до десятых."""
    
    totals = {}
    counts = {}
    
    # Проходим по всем "чистым" записям
    for record in records:
        city = record["city"]
        temp = record["temp"]
        
        # Считаем общую сумму температур для города (как было в старом скрипте)
        totals[city] = totals.get(city, 0) + temp
        # Считаем количество записей для города
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in totals:
        # Считаем среднее значение и округляем до 1 знака (до десятых)
        averages[city] = round(totals[city] / counts[city], 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:
    """Город с наибольшей средней температурой. При равенстве — первый по алфавиту."""
    
    # Чтобы не писать вычисления заново, просто вызываем нашу предыдущую функцию
    averages = average_by_city(records)
    
    best_city = ""
    # Задаем минимально возможное значение, чтобы любая реальная температура была больше
    best_temp = float("-100_000") 
    
    # Функция sorted() выстроит названия городов по алфавиту.
    # Это гарантирует, что при равенстве температур запишется первый по алфавиту город.
    for city in sorted(averages.keys()):
        # Строгое неравенство (>): если температура следующего города ТАКАЯ ЖЕ, 
        # то условие не выполнится, и в best_city останется предыдущий (по алфавиту) город.
        if averages[city] > best_temp:
            best_temp = averages[city]
            best_city = city
            
    return best_city

