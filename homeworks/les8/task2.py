"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""

class SameDivZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def same_div(parm1: int, parm2: int):
    if parm2 == 0:
        raise SameDivZeroError("Деление на 0")
    else:
        return parm1/parm2


if __name__ == '__main__':

    parm1 = 3
    parm2 = 0
    try:
        print(same_div(parm1, parm2))
    except SameDivZeroError as e:
        print(f"Произошла исключительная ситуация. {e.txt}")
    else:
        print("Успешное деление")


