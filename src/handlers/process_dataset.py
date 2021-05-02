import json
import csv

def start(name_of_dataset, function):
    file = open(f'resources/datasets/{name_of_dataset}.csv', 'r', encoding='utf-8')
    json_file = open(f'resources/datasets/{name_of_dataset}.json', 'w')
    
    file_content = csv.reader(file, delimiter=',')
    keys, data = next(file_content), list(file_content)
    
    data = list(filter(function,data))

    new_data = []
    for element in data:
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = element[i]
        new_data.append(dict)
    
    json.dump(new_data,json_file,indent=4)

    file.close()
    json_file.close()
