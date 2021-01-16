'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

my_list = [34, 343, 343, 12, 56, 676, 343, 565, 454]
print(f'Набор чисел = {my_list}')
with open(r'text_task_5.txt', 'w+') as f_obj:
    for element in my_list:
        f_obj.write(''.join(str(element) + ' '))
    f_obj.seek(0)
    sum_number = sum(map(int, f_obj.readline().split()))
    print(f'Сумма чисел = {sum_number}')
