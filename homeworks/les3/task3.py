"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
сумму наибольших двух аргументов.
"""

def my_func(var1: float, var2: float, var3: float) -> float:
    return max(var1, var2) + max(min(var1, var2), var3)

print("Складываем два наибольших числа из трех")
temp_input = { 1: ["Введите первое число: ", float, 0],
               2: ["Введите второе число: ", float, 0],
               3: ["Введите второе число: ", float, 0]}

for key, input_value in temp_input.items():
    while True:
        try:
            input_value[2] = input_value[1](input(input_value[0]))
            break
        except ValueError:
            print("Введено неверное значение. Попробуйте еще раз.")

print(f"Результат: {my_func(temp_input[1][2], temp_input[2][2], temp_input[3][2])}")
