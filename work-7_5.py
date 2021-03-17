import os
from json import dump

def stat_maker(path):
    stat = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            size = os.path.getsize(file_name)
            index = 10 ** len(str(size))
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if index in stat:
                if ext in stat[index][1]:
                    stat[index] = (stat[index][0] + 1, stat[index][1])
                else:

                    print(index, stat)
                    print(type(stat[index][1]))
# Здесь не работает
                    stat[index] = (stat[index][0] + 1, stat[index][1].append(ext))
            else:
                stat[index] = (1, [ext])

    sorted_stat = {}
    for i in sorted(stat.keys()):
        sorted_stat[i] = stat[i]
    return sorted_stat


path = 'C:\\Windows\\Media'
file_name = os.path.basename(path) + '_summary.json'

if not os.path.exists(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        dump(stat_maker(path), f, ensure_ascii=False, indent=4)
    print(f'Данные выгружены в {file_name}')
else:
    print(f'Невозможно сохранить данные: {file_name} - файл существует');
    print(stat_maker(path))
