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

csv_to_records("id,город\n1,Азов\n\n2,Шахты\n")