# Task 3

import os
from pprint import pprint

list_files = ['1.txt', '2.txt', '3.txt']
LOG_CATALOG_NAME = "sorted"
BASE_PATH = os.getcwd()

list = []
for file_name in list_files:
    full_path = os.path.join(BASE_PATH, LOG_CATALOG_NAME, file_name)
    with open(full_path, encoding='utf-8') as file:
        data = file.readlines()
        list.append((file_name, len(data), data))
list_sorted = sorted(list, key=lambda list: list[1])

file_name_total = 'total.txt'
full_path = os.path.join(BASE_PATH,file_name_total)
with open(full_path, 'a', encoding='utf-8') as file_total:
    for data in list_sorted:
        file_total.write(f"{data[0]}\n")
        file_total.write(f"{data[1]}\n")
        for i in data[2]:
            file_total.write(f"{i}")
        file_total.write(f"\n")



