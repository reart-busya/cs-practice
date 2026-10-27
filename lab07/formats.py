def csv_to_records(text: str) -> list[dict]:
    
    lines = [line.strip() for line in text.splitlines() if line.strip()]:
    if not lines:
        return []
    
    zogolovok = lines[0].split(",")
    records = []
    
    for line in lines[1:]:
        values = line.split(",")
        record = {zogolovok[i]: values[i] for i in range(len(zogolovok))}
        records.append(record)
        
    return records