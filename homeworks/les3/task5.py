"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""

def my_sum(list_float_values : list):
    return sum(list_float_values)

print("Суммируем значения")
temp_input = {1: ["Введите числа разделенные пробелом", ""], 2: "~"}

need_input = True
res_sum = 0.0

while need_input:
    input_value = temp_input[1]
    input_value[1] = input(f"{input_value[0]} (спецсимвол - '{temp_input[2]}'): ")

    if (input_value[1]) :
        list_value = input_value[1].split(" ")

        args_list = []

        for item_value in list_value:

            if item_value != temp_input[2] :
                try:
                    float_value = float(item_value)
                    args_list.append(float_value)
                except ValueError:
                    continue
            else:
                need_input = False
                break


        res_sum += my_sum(tuple(args_list))
        print(res_sum)

    else:
        need_input = False


print(f"Результат: {res_sum}")
