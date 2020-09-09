"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

input_info1 = "Введите любое число: "
input_info2 = "Введите еще одно число: "
input_info3 = "И еще одно: "

input_int1 = 0
input_int2 = 0
input_int3 = 0

input_value = input(input_info1)

if input_value.isdigit():
    input_int1 = int(input_value)
else:
    print("Это не число")


input_value = input(input_info2)
if input_value.isdigit():
    input_int2 = int(input_value)
else:
    print("Это не число")

input_value = input(input_info3)
if input_value.isdigit():
    input_int3 = int(input_value)
else:
    print("Это не число")

print("Твои введенные числа:", input_int1, input_int2, input_int3)