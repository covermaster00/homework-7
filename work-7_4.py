import os

def stat_maker(path):
    stat = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            size = os.path.getsize(file_name)
            index = 10 ** len(str(size))
            if index in stat:
                stat[index] += 1
            else:
                stat[index] = 1
    sorted_stat = {}
    for i in sorted(stat.keys()):
        sorted_stat[i] = stat[i]
    return sorted_stat


print(stat_maker('C:\\Windows\\Media'))
