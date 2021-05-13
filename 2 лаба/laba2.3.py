# Задан  путь  к директории с музыкальными файлами(в  названии которых  нет  номеров,  а  только  названия  песен) и
# текстовый  файл, хранящийполный список песен с номерами и названиямив видестрок формата «01.Freefall[6:12]».
# Напишите скрипт, который корректирует имена файловв директории на основе текста списка песен.


import os


dir_path = 'музыка'
file_in_dir = os.listdir(path=dir_path)
open_file = open('треклист.txt', 'r')
data_from_file = open_file.read()
data_from_file = data_from_file.split('\n')
open_file.close()
print(file_in_dir)
print(data_from_file)
os.chdir('музыка')
for i in file_in_dir:
    for j in data_from_file:
        if i in j:
            os.rename(i, j)
