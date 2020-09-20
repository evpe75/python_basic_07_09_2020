"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

def calc_salary(work_hours: int, rate: float, prize: float) -> float:
    """
    Вычисляет заработную пплату
    :param work_hours: выработка в часах
    :param rate: ставка в час
    :param prize: премия
    :return: зарплата замесяц
    """
    return work_hours * rate + prize, 2

_, arg_work_hours, arg_rate, arg_prize = argv

print(f"Заработная плата = {calc_salary(int(arg_work_hours), float(arg_rate), float(arg_prize))}")