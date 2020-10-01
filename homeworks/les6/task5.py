"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print(f"Пишет {self._title}.")


class Pen(Stationery):
    def __init__(self):
        super().__init__("ручка")

    def draw(self):
        super().draw()
        print("Ручку не сотрешь!")

class Pencil(Stationery):
    def __init__(self):
        super().__init__("карандаш")

    def draw(self):
        super().draw()
        print("Это можно стретерь")

class Handle(Stationery):
    def __init__(self):
        super().__init__("маркер")

    def draw(self):
        super().draw()
        print("Ярко и красиво")


if __name__ == '__main__':
    pen1 = Pen()
    pen1.draw()
    print("\n")

    pencil1 = Pencil()
    pencil1.draw()
    print("\n")

    handle1 = Handle()
    handle1.draw()
    print("\n")
