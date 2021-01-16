'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open(r'text_task_4_2.txt', 'w', encoding='utf-8') as f_obj_temp:
    with open(r'text_task_4.txt', encoding='utf-8') as f_obj:
        f_obj.seek(0)
        for line in f_obj:
            f_obj_temp.write(''.join([my_dict[line.split()[0]], line.strip()[-4:], '\n']))
