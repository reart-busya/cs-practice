def csv_to_records(text: str) -> list[dict]:

    rezult = []
    lines = []

    lines = text.split('\n')

    zogolovok = [item.strip() for item in lines[0].split(',')]
    values = []

    for line in lines[1:]:
        if line != "":
            dict_rez = {}
            values = [item.strip() for item in line.split(',')]
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
                    value = parts[1].split('#')[0].strip()
                    if value == "true" or value == "yes":
                        rezult[key] = True
                    elif value == "false" or value == "no":
                        rezult[key] = False
                    elif value.isdigit():
                        rezult[key] = int(value)
                    elif ',' in value:
                        number_parts = value.split(',')
                        if len(number_parts) == 2 and number_parts[0].isdigit() and number_parts[1].isdigit():
                            rezult[key] = float(value.replace(',', '.'))
                        else:
                            rezult[key] = value
                    elif '.' in value:
                        try:
                            rezult[key] = float(value)
                        except ValueError:
                            rezult[key] = value
                    elif value == '':
                        rezult[key] = []
                        list_key = key
                    else:
                       rezult[key] = value

    return rezult

print(parse_settings(["rate: 3,5 # с запятой"]))

def merge_by_key(rows: list[dict], extra: list[dict], key: str = "id") -> list[dict]:

    rezult = []

    for row in rows:
        new_row = row
        for extr in extra:
            if key in row and key in extr and row[key] == extr[key]:
                for ext_key in extr:
                    if ext_key not in row:
                        new_row[ext_key] = extr[ext_key]

        rezult.append(new_row)

    return rezult

import json


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)

# ensure_ascii для кирилицы
# indent для отступов