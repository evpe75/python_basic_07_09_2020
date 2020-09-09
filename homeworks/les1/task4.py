'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

input_info = "Введите положительное целое число: "
str_value = input(input_info)
max_digit = 0

if str_value.isdigit():
    cur_value = int(str_value)
    while cur_value > 0:
        cur_digit = cur_value %10
        print(cur_digit)
        cur_value //= 10
        if (cur_digit > max_digit):
            max_digit = cur_digit

    print(f"Максимальная цифра: {max_digit}")
else:
    print("Введено не число")
