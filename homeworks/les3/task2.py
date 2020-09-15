"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def person_info(first_name: str, last_name: str, birthday_year: int, city: str, email: str, phone: str) -> str:
    return format(f"Имя: {first_name}, Фамилия: {last_name}, Год рождения: {birthday_year}, Город: {city}, E-mail: "
                  f"{email}, Телефон: {phone}")


temp_input = {("Введите имя: ", str): "",
              ("Введите фамилию: ", str): "",
              ("Введите год рожденья: ", int): 0,
              ("Введите город проживания: ", str): "",
              ("Введите e-mail: ", str): "",
              ("Введите телефон: ", str): ""}

print("Начинаем сбор персональных данных")

for item_input_info in temp_input.keys():
    while True:
        try:
            input_value = item_input_info[1](input(item_input_info[0]))
            temp_input[item_input_info] = input_value
            break
        except ValueError:
            print("Введено неверное значение. Попробуйте еще раз.")

keys = list(temp_input.keys())

result = person_info(first_name = temp_input[keys[0]], last_name = temp_input[keys[1]], birthday_year = temp_input[keys[2]],
                     city = temp_input[keys[3]], email = temp_input[keys[4]], phone = temp_input[keys[5]])
print(f"Были введены следующие данные:\n{result}")
