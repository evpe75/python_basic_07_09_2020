"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
input_repeat_info = "Попробуйте еще раз. И помните - это в ваших же интересах"
input_info1 = "Будьте добры, введите целое положительное значение выручки вашей компании: "
input_info2 = "Будьте добры, введите целое положительное значение издержек вашей компании: "

debet = 0
credit = 0
profit = 0

input_value = input(input_info1)
while not input_value.isdigit():
    print(input_repeat_info)
    input_value = input(input_info1)

debet = int(input_value)

input_value = input(input_info2)
while not input_value.isdigit():
    print(input_repeat_info)
    input_value = input(input_info2)

credit = int(input_value)

profit = debet - credit

if profit > 0:
    rental = profit/debet

    print(f"Прибыль вашей компании = {profit}")
    print(f"Рентабельность вашей компании = {rental}")

    input_info3 = "Будьте добры, введите количество сотрудников вашей компании: "
    input_value = input(input_info2)
    while not input_value.isdigit():
        print(input_repeat_info)
        input_value = input(input_info2)

    empl_count = int(input_value)

    empl_profit = rental/empl_count
    print(f"Рентабельность вашей компании на сотрудника = {empl_profit}")

else:
    print(f"Убыток вашей компании = {profit}")









# print("Твои введенные числа:", input_int1, input_int2, input_int3)