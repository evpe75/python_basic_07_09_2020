"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

firm_dict = {}
average_profit = 0

with open("text_task7.txt", "r", encoding="UTF-8") as firm_file:
    for item in firm_file:
        [firm_name, _, debet, credit] = item.split(" ")
        if int(debet) > int(credit):
            profit = int(debet) - int(credit)
            firm_dict[firm_name] = profit
            average_profit += profit

print(firm_dict)

firm_list = []

if len(firm_dict):
    firm_list = [firm_dict, {"average_profit" : average_profit / len(firm_dict)}]

print(firm_list)

with open("test_task7.json", "w") as json_firm_list:
    json.dump(firm_list, json_firm_list)

