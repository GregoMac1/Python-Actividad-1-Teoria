import json
import csv

def start(name_of_dataset):
    file = open(f'resources/datasets/{name_of_dataset}.csv', 'r', encoding='utf-8')
    json_file = open(f'resources/datasets/{name_of_dataset}.json', 'w')
    
    file_content = csv.reader(file, delimiter=',')
    keys, data = next(file_content), list(file_content)

    data = list(filter(lambda match: (match[1] == 'Argentina' or match[2] == 'Argentina') and match[5] == 'FIFA World Cup' and (match[0].startswith('1978') or match[0].startswith('1986')),data))

    new_data = []
    for match in data:
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = match[i]
        new_data.append(dict)
    
    json.dump(new_data,json_file,indent=4)

    file.close()
    json_file.close()
