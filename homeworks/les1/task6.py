"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

input_repeat_info = "Попробуйте еще раз. И помните - это в ваших же интересах"
input_info1 = "Введите какой результат в полных километрах был у спортсмена в первый день: "
input_info2 = "Введите какой результат в полных километрах нужен: "

input_value = input(input_info1)
while not input_value.isdigit():
    print(input_repeat_info)
    input_value = input(input_info1)

a = int(input_value)

input_value = input(input_info2)
while not input_value.isdigit():
    print(input_repeat_info)
    input_value = input(input_info1)

b = int(input_value)

print(f"a = {a}, b = {b}")
print(f"1-й день: {a}")
day_result = float(a)
idx = 1
while day_result < b:
    idx += 1
    day_result += day_result* 0.1
    print("{}-й день: {:.2f}".format(b, day_result))

print(f"Ответ: на {idx}-й день спортсмен достиг результата — не менее {b} км")

