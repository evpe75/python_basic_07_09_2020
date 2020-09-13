"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
"""

var_rates = [10, 9, 6, 3, 2]

print(var_rates)

input_value = None

while (input_value is None or not input_value.isdigit()):
    if not input_value is None:
        print("Введено не целое число, попробуйте еще раз")

    input_value = input("Введите новый рейтинг в виде целого числа: ")

if var_rates.count(int(input_value)):
    idx = var_rates.index(int(input_value))
    print(idx)
    var_rates.insert(idx + var_rates.count(int(input_value)), int(input_value))
else:
    idx = 0
    for list_value in var_rates:
        if list_value < int(input_value):
            break
        else:
            idx += 1
    var_rates.insert(idx, int(input_value))


print(var_rates)

