"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""

import time


class TrafficLight:

    __dictColorTimes = {'red': 7, 'yellow': 2, 'green': 5}


    def __init__(self, maxChangeCount):
        self.__stages = [item for item in TrafficLight.__dictColorTimes.keys()]
        self.__color = self.__stages[1]
        self.__prev_color = self.__stages[2]
        self.__endTime = 0
        self.__maxChangeCount = maxChangeCount


    def _changeColor(self):
        if self.__color == 'red' or self.__color == 'green' :
            self.__prev_color = self.__color
            self.__color = 'yellow'
        elif self.__color == 'yellow' :
            if self.__prev_color == 'red' :
                self.__prev_color = self.__color
                self.__color = 'green'
            else :
                self.__prev_color = self.__color
                self.__color = 'red'

        print(self.__color)

        self.__endTime = time.time() + self.__dictColorTimes[self.__color]


    def running(self):
        self._changeColor()
        count = 0
        while True:
            if self.__endTime < time.time():
                self._changeColor()
                count += 1
                if count > self.__maxChangeCount :
                    break


if __name__ == '__main__':
    trafic1 = TrafficLight(10)
    trafic1.running()

    # print(time.time())
    # time.sleep(10)
    # print(time.time())
