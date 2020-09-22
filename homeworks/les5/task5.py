"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from functools import reduce


def my_sum(a: int, b: int) -> int:
    return a+b


numbers = [item for item in range(1, 151)]
str_numbers = [str(item) for item in numbers]
# print(" ".join(str_numbers))

with open("text_task5.txt", "w", encoding="UTF-8") as numbers_file:
    numbers_file.write(" ".join(str_numbers))

print(reduce(my_sum, numbers))