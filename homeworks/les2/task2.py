"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

input_value = None

while (input_value is None or not input_value.isdigit()):
    if not input_value is None:
        print("Введено не целое число, попробуйте еще раз")

    input_value = input("Введите количество элементов списка: ")

idx = 1
var_list = []

while idx <= int(input_value):
    list_item = input(f"Введите значение элемента списка {idx}: ")
    var_list.append(list_item)

    idx += 1

print(var_list)

list_var = []

idx = 0
while idx < len(var_list)//2:
    list_var.extend([var_list[idx*2 +1], var_list[idx*2]])
    idx += 1;

if (len(var_list) % 2):
    list_var.append(var_list[len(var_list)-1])

print("Результат")
print(list_var)

