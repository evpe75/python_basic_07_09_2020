"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, type):
        self._type = type


    @property
    def type(self):
        return self._type


    @property
    @abstractmethod
    def issue(self):
        pass

class Coat(Clothes):
    __parm1 = 6.5
    __parm2 = 0.5

    def __init__(self,v):
        super().__init__('пальто')
        self._v = v

    @property
    def issue(self):
        return f"Расход для {self.type} - {self._v/self.__parm1 + self.__parm2}"


class Suit(Clothes):
    __parm1 = 2
    __parm2 = 0.3

    def __init__(self, h):
        super().__init__('костюм')
        self._h = h

    @property
    def issue(self):
        return f"Расход для {self.type} - {self.__parm1 * self._h + self.__parm2}"


if __name__ == '__main__':
    coat = Coat(3)
    print(coat.issue)

    suit = Suit(3)
    print(suit.issue)