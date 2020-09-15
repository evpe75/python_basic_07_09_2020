"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_div(var1, var2):
    return var1/var2

temp_input = { ("Введите делимое: ", float) : 0, ("Введите делитель: ", float) : 0}

print("Начинаем делить числа")

iteration_idx = 0

while True :
    iteration_idx += 1

    for item_input_info in temp_input.keys() :
        while True:
            try:
                input_value = item_input_info[1](input(item_input_info[0]))
                temp_input[item_input_info] = input_value
                break
            except ValueError:
                print("Введено не число. Попробуйте еще раз.")

    keys = list(temp_input.keys())

    try:
        print(f"Результат выполнения функции my_div: {my_div(temp_input[keys[0]], temp_input[keys[1]])}")
        break
    except ZeroDivisionError :
        print("Делить на ноль нельзя. Ты в школе вообще учился?. Попробуем еще раз.")
    except:
        if iteration_idx < 5:
            print("Что-то пошло не так. Пробуем еще")
        else:
            break