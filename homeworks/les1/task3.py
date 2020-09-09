'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
out_value = 0

input_info = "Введите число: "
str_value = input(input_info)

if str_value.isdigit():
    idx = 1
    while idx <= 3:
        out_value += int(str_value*idx)
        idx += 1

    print(f"Результат : {out_value}")

else:
    print("Введено не число")
