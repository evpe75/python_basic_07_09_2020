"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from functools import reduce


def my_sum(a: int, b: int) -> int:
    return a+b


with open("text_task6.txt", "r", encoding="UTF-8") as list_subj:
    subj_items = {str(item).split(":")[0] : str(item).split(":")[1] for item in list_subj}

for idx, text_value in subj_items.items() :
    item_values = "".join([char for char in text_value if char in "0123456789 "]).split(" ")
    item_hours = [int(value) for value in item_values if value ]
    subj_items[idx] = reduce(my_sum, item_hours)

print(subj_items)
