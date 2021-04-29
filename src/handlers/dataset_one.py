import json
import csv

def start(name_of_dataset):
    file = open(f'resources/datasets/{name_of_dataset}.csv', 'r')
    json_file = open(f'resources/datasets/{name_of_dataset}.json', 'w')
    
    file_content = csv.reader(file, delimiter=',')
    keys, data = next(file_content), list(file_content)

    data = list(filter(lambda song: song[2] == 'Foo Fighters' and 2000 <= int(song[3]) < 2010, data))

    new_data = []
    for song in data:
        dict = {}
        for i,j in zip(keys,data):
            dict[i] = j
        new_data.append(dict)
    
    json.dump(new_data,json_file)

    file.close()
    json_file.close()
