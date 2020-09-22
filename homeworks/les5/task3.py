"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from functools import reduce


def my_sum(a: float, b: float) -> float:
    return a+b


def my_sum_str(a, b):
    return f"{a}, {b}"


with open("text_task3.txt", "r", encoding="UTF-8") as salary_file:
    items = [str(item).split(": ")[0] for item in salary_file if float(str(item).split(": ")[1]) < 20000 ]


with open("text_task3.txt", "r", encoding="UTF-8") as salary_file:
    sals = [float(str(item).split(": ")[1]) for item in salary_file]


# print(items)
# print(sals)

print(f"Сотрудники c з/п меньше 20000: {reduce(my_sum_str, items)}")
print(f"Средняя з/п: {reduce(my_sum, sals)/len(sals) if len(sals) > 0 else 0}")