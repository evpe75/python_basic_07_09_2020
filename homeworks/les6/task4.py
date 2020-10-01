"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

class Car:

    def __init__(self, color: str, name: str, is_police: bool):
        self._color = color
        self._name = name
        self._is_police = is_police
        self._speed = 0

    def go(self, speed: int):
        self._speed = speed
        print(f"{'Полицейская машина' if self._is_police else 'Mашина'} {self._name} цвета {self._color} поехала со скоростью {self._speed} км/ч")

    def stop(self):
        if self._speed == 0 :
            print(f"{'Полицейская машина' if self._is_police else 'Mашина'} {self._name} цвета {self._color} и так стоит")
        else:
            print(f"{'Полицейская машина' if self._is_police else 'Mашина'} {self._name} цвета {self._color} остановилась")

        self._speed = 0

    def turn(self, direction: str):
        print(f"{'Полицейская машина' if self._is_police else 'Mашина'} {self._name} цвета {self._color} повернула {direction}")

    def show_speed(self):
        print(f"Скорость {'полицейской машины' if self._is_police else 'машины'} {self._name} цвета {self._color} - {self._speed} км/ч")



class SportCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name, True)


class TownCar(Car):

    __max_speed = 60

    def __init__(self, color: str, name: str):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed();
        if self._speed > self.__max_speed:
            print(f"!!!Скорость превышена на {self._speed - self.__max_speed} км/ч. Максимально разрешенная скорость для {self._name} {self.__max_speed} км/ч")


class WorkCar(TownCar):

    __max_speed = 40

    def __init__(self, color: str, name: str):
        super().__init__(color, name)



if __name__ == '__main__':
    policeCar1 = PoliceCar('синяя', 'Ford')
    policeCar1.go(50)
    policeCar1.show_speed()
    policeCar1.go(100)
    policeCar1.show_speed()
    policeCar1.go(120)
    policeCar1.show_speed()
    policeCar1.turn("направо")
    policeCar1.show_speed()
    policeCar1.turn("налево")
    policeCar1.show_speed()
    policeCar1.stop()
    policeCar1.show_speed()
    policeCar1.stop()
    policeCar1.show_speed()

    print("\n")

    sportCar1 = SportCar('красная', 'Мазератти')
    sportCar1.go(50)
    sportCar1.show_speed()
    sportCar1.go(100)
    sportCar1.show_speed()
    sportCar1.go(120)
    sportCar1.show_speed()
    sportCar1.turn("направо")
    sportCar1.show_speed()
    sportCar1.turn("налево")
    sportCar1.show_speed()
    sportCar1.stop()
    sportCar1.show_speed()
    sportCar1.stop()
    sportCar1.show_speed()

    print("\n")

    townCar1 = TownCar('черная', 'Камаз')
    townCar1.go(50)
    townCar1.show_speed()
    townCar1.go(100)
    townCar1.show_speed()
    townCar1.go(120)
    townCar1.show_speed()
    townCar1.turn("направо")
    townCar1.show_speed()
    townCar1.turn("налево")
    townCar1.show_speed()
    townCar1.stop()
    townCar1.show_speed()
    townCar1.stop()
    townCar1.show_speed()

    print("\n")

    workCar1 = WorkCar('черная', 'Эксковатор')
    workCar1.go(50)
    workCar1.show_speed()
    workCar1.go(100)
    workCar1.show_speed()
    workCar1.go(120)
    workCar1.show_speed()
    workCar1.turn("направо")
    workCar1.show_speed()
    workCar1.turn("налево")
    workCar1.show_speed()
    workCar1.stop()
    workCar1.show_speed()
    workCar1.stop()
    workCar1.show_speed()
