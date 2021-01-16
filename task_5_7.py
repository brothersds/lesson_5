'''
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''

import json

with open(r'text_task_7.txt', encoding='utf-8') as f_obj:
    f_obj.seek(0)
    count, average_profit = 0, 0
    my_dict, avg_profit_dict = {}, {}
    for element in f_obj:
        company_profit = float(element.split()[2]) - float(element.split()[3])
        if company_profit > 0:
            count += 1
            average_profit += company_profit
        my_dict[element.split()[0]] = company_profit
    avg_profit_dict['average_profit'] = round(average_profit / count, 2)
    print(f'{[my_dict, avg_profit_dict]}')
with open(r'text_task_7.json', 'w+', encoding='utf-8') as f_obj:
    json.dump([my_dict, avg_profit_dict], f_obj)
with open(r'text_task_7.json', encoding='utf-8') as f_obj:
    data = json.load(f_obj)

