import json
import csv

def start(name_of_dataset):
    file = open(f'resources/datasets/{name_of_dataset}.csv', 'r')
    json_file = open(f'resources/datasets/{name_of_dataset}.json', 'w')
    
    file_content = csv.reader(file, delimiter=',')
    keys, data = next(file_content), list(file_content)

    data = list(filter(lambda match: 'Argentina' in (match[1],match[2]) and match[5] == 'FIFA World Cup' and (match[0].startswith('1978') or match[0].startswith('1986'))))

    new_data = []
    for match in data:
        dict = {}
        for i,j in zip(keys,data):
            dict[i] = j
        new_data.append(dict)
    
    json.dump(new_data,json_file)

    file.close()
    json_file.close()
