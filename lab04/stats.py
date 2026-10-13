def parse_record(line: str) -> dict:

    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно три поля, разделенных \";\" ")
    
    city = parts[0].strip()
    temp_str = parts[1].strip().replace(",", ".")
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")
    
    try:
        temp = float(temp_str)
    except ValueError:

        raise ValueError(f"Температура не является числом: '{temp_str}'")
    
    return {
        "city": city,
        "temperature": temp,
        "date": date
    }

def read_valid(lines: list[str]) -> list[dict]:
    
    valid_records = []
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
            
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temp = record["temperature"]

        totals[city] = totals.get(city, 0) + temp
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:

    averages = average_by_city(records)
    
    best_city = ""
    best_temp = float("-100_000") 
    
    for city in sorted(averages.keys()):
        if averages[city] > best_temp:
            best_temp = averages[city]
            best_city = city
            
    return best_city

