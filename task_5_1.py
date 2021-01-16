'''
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''

import os.path

with open('text.txt', 'a+') as f_obj:
    while True:
        if not f_obj.write(input()):
            break
        else:
            continue
    f_obj.seek(0)
    for line in f_obj:
        print(line)
os.remove('text.txt')
