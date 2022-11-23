import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename):
    delimiter = ','
    new_line = '\n'
    input_str = ''
    list_of_dicts = []
    with open(filename) as fi:
        for line in fi:
            input_str = input_str + line
        rows = input_str.split(new_line)
        headers, rows = rows[:1], rows[1:]
        headers = headers[0].split(delimiter)
        rows = [i.split(delimiter) for i in rows if i != '']

    length = len(headers)
    for row in rows:
        dict_ = {headers[i]: row[i] for i in range(length)}
        list_of_dicts.append(dict_)

    return list_of_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
