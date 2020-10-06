"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class DateValueError(Exception):

    def __int__(self, txt):
        self.txt = txt


class Date:

    _max_days = {1: 31, 2:29, 3:31, 4: 30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"'{self.__year:>04}-{self.__month:>02}-{self.__day:>02}'"


    @staticmethod
    def check_date_value(day: str, month: str, year: str) -> bool:
        if not year.isdigit() or int(year) > 2999 or int(year) < 0 :
            return False

        if not month.isdigit() or int(month) > 12 or int(month) < 0 :
            return False

        if not day.isdigit() or int(day) > Date._max_days[int(month)] or int(day) < 0 :
            return False

        return True


    @classmethod
    def construct(cls, date: str):
        list_date = date.split("-", 3)
        if not len(list_date) == 3 or not Date.check_date_value(list_date[0], list_date[1], list_date[2]):
            raise DateValueError(f"Неверный формат даты {date}")
        else:
            return cls(int(list_date[0]), int(list_date[1]), int(list_date[2]))



if __name__ == '__main__':
    date1 = Date.construct("05-1-2020")
    print(date1)

    date2 = Date.construct("31-12-2020")
    print(date2)

    date2 = Date.construct("30-2-2021")
    print(date2)
