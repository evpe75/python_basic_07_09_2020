"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

input_info = "Введите количество секунд: "

seconds = 0
minutes = 0
hours = 0

input_value = input(input_info)

if input_value.isdigit():
    seconds = int(input_value)
    hours   = seconds//3600
    seconds %= 3600
    minutes = seconds//60
    seconds %= 60

    hours_str = str(hours)
    minutes_str = str(minutes)
    seconds_str = str(seconds)

    if len(hours_str) < 2:
        hours_str = f"0{hours_str}"
    if len(minutes_str) < 2:
        minutes_str = f"0{minutes_str}"
    if len(seconds_str) < 2:
        seconds_str = f"0{seconds_str}"

    print(f"Время : {hours_str}:{minutes_str}:{seconds_str}")


else:
    print("Введено не число")
