import json
import csv

def start(name_of_dataset):
    file = open(f'resources/datasets/{name_of_dataset}.csv', 'r')
    json_file = open(f'resources/datasets/{name_of_dataset}.json', 'w')
    
    file_content = csv.reader(file, delimiter=',')
    keys, data = next(file_content), list(file_content)

    data = list(filter(lambda song: song[2] == 'Foo Fighters' and 2000 <= int(song[3]) < 2010, data))

    new_data = [
        {
            f'{keys[0]}':song[0],
            f'{keys[1]}':song[1],
            f'{keys[2]}':song[2],
            f'{keys[3]}':song[3],
            #f'{keys[4]}':song[4],
            #f'{keys[5]}':song[5],
            #f'{keys[6]}':song[6],
            #f'{keys[7]}':song[7],
            #f'{keys[8]}':song[8],
            #f'{keys[9]}':song[9],
            #f'{keys[10]}':song[10],
            #f'{keys[11]}':song[11],
            #f'{keys[12]}':song[12],
            #f'{keys[13]}':song[13],
            #f'{keys[14]}':song[14],
            #f'{keys[15]}':song[15],
            #f'{keys[16]}':song[16],
            #f'{keys[17]}':song[17]
        }
        for song in data
    ]
    
    json.dump(new_data,json_file)

    file.close()
    json_file.close()
