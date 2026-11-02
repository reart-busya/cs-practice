def csv_to_records(text: str) -> list[dict]:

    rezult = []
    lines = []

    lines = text.split('\n')

    zogolovok = lines[0].split(',')
    values = []

    for line in lines[1:]:
        if line != "":
            dict_rez = {}
            values = line.split(',')
            for i in range(len(zogolovok)):
                dict_rez[zogolovok[i]] = values[i]
            rezult.append(dict_rez)

    return rezult

def parse_settings(lines: list[str]) -> dict:

    rezult = {}
    list_key = None

    for line in lines:
        if line.strip().startswith("-"):
            list_value = line.strip()[2:].strip()
            rezult[list_key].append(list_value)
        else:
            if not line.startswith("#"):
                parts = line.split(':')
                if len(parts) >= 2:
                    key = (parts[0].strip())
                    value = (parts[1].strip())
                    if value == "true" or value == "yes":
                        rezult[key] = True
                    elif value == "false" or value == "no":
                        rezult[key] = False
                    elif value.isdigit():
                        rezult[key] = int(value)
                    elif '.' in value:
                        rezult[key] = float(value)
                    elif value == '':
                        rezult[key] = []
                        list_key = key
                    else:
                       rezult[key] = value

    return rezult

print(parse_settings(lines = [
    "# отчёт",
    "title: Отчёт за март",
    "decimals: 1",
    "active: true",
    "columns:",
    "  - город",
    "  - цена"
]))
