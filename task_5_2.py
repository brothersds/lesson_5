'''
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''

with open(r'text_task_2.txt', 'a+', encoding='utf-8') as f_obj:
    f_obj.seek(0)
    lines_in_text = len(f_obj.readlines())
    print(f'Кол-во строк = {lines_in_text}')
    f_obj.seek(0)
    for index, value in enumerate(f_obj, start=1):
        words_in_line = len(value.split())
        print(f'Количество слов в строке = {index} равно = {words_in_line}')
