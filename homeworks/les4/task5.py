"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()
"""

from functools import reduce

def my_func(a, b):
    return a*b

my_list = [item for item in range(100, 1001) if item & 1 == 0]

print(my_list)

print(reduce(my_func, my_list))