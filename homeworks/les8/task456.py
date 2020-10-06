"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

from abc import ABC, abstractmethod


class OfficeEquipment(ABC):

    def __init__(self, type, mark, model, color, volume):
        self._type = type
        self._mark = mark
        self._model = model
        self._color = color
        self._volume = volume

    def __str__(self):
        return f"{self._type.title()} марки {self._mark} модели {self._model} цвета {self._color}"

    @abstractmethod
    def run(self):
        pass

    @property
    def type(self):
        return self._type

    @property
    def mark(self):
        return self._mark

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @property
    def volume(self):
        return self._volume

    @classmethod
    def get_dict(cls) -> dict:
        return {}

    @classmethod
    def get_volume(cls, mark, model):
        if (mark, model) in cls.get_dict().keys():
            return cls.get_dict()[(mark, model)]['volume']
        else:
            return 0

    @classmethod
    def check_exists_model(cls, mark, model, color) -> bool:
        check_result = False
        if (mark, model) in cls.get_dict().keys():
            print_parm = cls.get_dict()[(mark, model)]
            if color in print_parm["colors"]:
                check_result = True

        return check_result


class OfficeEquipmentNotExistsError(Exception):

    def __init__(self, type, mark, model, color):
        self.txt = f"Ошибка!!! Офисное оборудование {type} марки {mark} модели {model} цвета {color} не существует"


class Printer(OfficeEquipment):

    _dict_printer_models = {('Pantum', 'P2200'): {"colors": ['black', 'wite', 'grey'], 'volume': 0.1},
                            ('Pantum', 'P2500'): {"colors": ['black', 'grey'], 'volume': 0.15},
                            ('Pantum', 'P3010'): {"colors": ['wite'], 'volume': 0.2},
                            ('HP', 'Laser 107'): {"colors": ['wite', 'grey'], 'volume': 0.13},
                            ('HP', 'Laser 1202'): {"colors": ['black', 'grey'], 'volume': 0.15},
                            ('HP', 'Laser 1202'): {"colors": ['black', 'grey'], 'volume': 0.16},
                            ('Brother', 'L2300DR'): {"colors": ['black', 'grey'], 'volume': 0.15},
                            ('Brother', 'L2340DR'): {"colors": ['black'], 'volume': 0.2},
                            ('Brother', 'L3230CDW'): {"colors": ['wite', 'grey'], 'volume': 0.18}
                            }

    def __init__(self, mark, model, color, volume):
        super().__init__('Printer', mark, model, color, volume)

    def run(self):
        print(f"Печатает {self._type}")

    @classmethod
    def get_dict(cls) -> dict:
        return Printer._dict_printer_models

    @classmethod
    def construct(cls, mark, model, color):

        if cls.check_exists_model(mark, model, color):
            return Printer(mark, model, color, cls.get_volume(mark, model))
        else:
            raise OfficeEquipmentNotExistsError('Printer', mark, model, color)


class Copier(OfficeEquipment):

    _dict_copier_models = {('Xerox ', '3025'): {"colors": ['wite', 'grey'], 'volume': 0.4},
                           ('Xerox', 'B215'): {"colors": ['black', 'grey'], 'volume': 0.5},
                           ('Xerox', 'P3010'): {"colors": ['wite'], 'volume': 0.6},
                           ('Xerox', 'P3011'): {"colors": ['wite', 'grey'], 'volume': 0.7}
                           }

    def __init__(self, mark, model, color, volume):
        super().__init__('Copier', mark, model, color, volume)

    def run(self):
        print(f"Копирует {self._type}")

    @classmethod
    def get_dict(cls) -> dict:
        return cls._dict_copier_models

    @classmethod
    def construсt(cls, mark, model, color):

        if cls.check_exists_model(mark, model, color):
            return Copier(mark, model, color, cls.get_volume(mark, model))
        else:
            raise OfficeEquipmentNotExistsError('Copier', mark, model, color)


class Scaner(OfficeEquipment):

    _dict_scaner_models = {('Canon', '3025'): {"colors": ['wite', 'grey'], 'volume': 0.15},
                           ('Canon', 'B215'): {"colors": ['black', 'grey'], 'volume': 0.1},
                           ('Epson', 'V19'): {"colors": ['wite'], 'volume': 0.12},
                           ('Epson', 'V370'): {"colors": ['wite', 'grey'], 'volume': 0.2}
                           }

    def __init__(self, mark, model, color, volume):
        super().__init__('Scaner', mark, model, color, volume)

    def run(self):
        print(f"Сканирует {self._type}")

    @classmethod
    def get_dict(cls) -> dict:
        return cls._dict_scaner_models

    @classmethod
    def construсt(cls, mark, model, color):

        if cls.check_exists_model(mark, model, color):
            return Copier(mark, model, color, cls.get_volume(mark, model))
        else:
            raise OfficeEquipmentNotExistsError('Scaner', mark, model, color)


class LocationFullError(Exception):
    def __init__(self, type, location_name, receipt_count: int, count: int):
        self.txt = f"{str(type).title()} '{location_name}' полон. Удалось принять {receipt_count} оборудования " \
                   f"из {count}"


class LocationNotContainEqupmentError(Exception):
    def __init__(self, type, location_name, equip: OfficeEquipment, issue_count: int, count: int):
        self.txt = f"{str(type).title()} '{location_name}' не содержит достаточного количество " \
                   f"оборудования {equip.type}"
        self.txt += f"марки {equip.mark} модели {equip.model} цвета {equip.color}. "
        self.txt += f"Удалось принять {issue_count} оборудования из {count}"


class Location:

    def __init__(self, name, type, max_volume):
        self._name = name
        self._type = type
        self._max_volume = max_volume
        self._full_volume = 0
        self._catalog = {}

    def __str__(self):
        return f"{str(self._type).title()} '{self._name}' {str(self._catalog)}"

    @property
    def free_volume(self):
        return self._max_volume - self._full_volume

    def count_equip(self, equip: OfficeEquipment) -> int:
        key_equip = (equip.type, equip.mark, equip.model, equip.color)
        if key_equip in self._catalog.keys():
            return self._catalog[key_equip]
        else:
            return 0

    def receipt(self, equip: OfficeEquipment, count: int):

        if count > 0:
            key_equip = (equip.type, equip.mark, equip.model, equip.color)
            if key_equip not in self._catalog.keys():
                self._catalog[key_equip] = 0

            receipt_count = 0
            for _ in range(count):
                if self._full_volume + equip.volume <= self._max_volume:
                    self._catalog[key_equip] += 1
                    self._full_volume += equip.volume
                    receipt_count += 1
                else:
                    raise LocationFullError(self._type, self._name, receipt_count, count)

    def issue(self, equip: OfficeEquipment, count: int):

        if count > 0:
            key_equip = (equip.type, equip.mark, equip.model, equip.color)
            if key_equip not in self._catalog.keys():
                self._catalog[key_equip] = 0

            issue_count = 0
            for _ in range(count):
                if self._catalog[key_equip] > 0 + equip.volume <= self._max_volume:
                    self._catalog[key_equip] -= 1
                    self._full_volume -= equip.volume
                    issue_count += 1
                else:
                    raise LocationNotContainEqupmentError(self._type, self._name, equip, issue_count, count)


class Store(Location):
    def __init__(self, name):
        super().__init__(name, "Магазин", 2)


class RemoteLocation(Location):
    def __init__(self, name):
        super().__init__(name, "Удаленный склад", 100)


class Transport(Location):
    def __init__(self, name):
        super().__init__(name, "Транспорт", 1)

    def transfer(self, from_location: Location, to_location: Location, equip: OfficeEquipment, count: int):

        key_equip = (equip.type, equip.mark, equip.model, equip.color)
        self._catalog[key_equip] = 0

        # Перегружаем оборудование с исходного склада в машину
        try:
            before_count = from_location.count_equip(equip)
            from_location.issue(equip, count)
        except LocationNotContainEqupmentError as ex:
            print(ex.txt)
        finally:
            issue_count = before_count - from_location.count_equip(equip)

        try:
            self.receipt(equip, issue_count)
        except LocationFullError as ex:
            print(ex.txt)
            from_location.receipt(equip, issue_count - self.count_equip(equip))

        # Выгружаем оборудование из машины на конечный склад
        trans_count = 0
        try:
            trans_count = self.count_equip(equip)
            self.issue(equip, trans_count)
            before_count = to_location.count_equip(equip)
            to_location.receipt(equip, trans_count)
        except LocationFullError as ex:
            print(ex.txt)
            self.receipt(equip, trans_count + before_count - to_location.count_equip(equip))

        # Возвращаем оставшееся в машине оборудование на исходный склад
        trans_count = self.count_equip(equip)
        if trans_count > 0:
            self.issue(equip, trans_count)
            from_location.receipt(equip, trans_count)


if __name__ == '__main__':

    try:
        print1 = Printer.construсt('Brother', 'L2340DR', 'black')
        print(print1)

        rem_loc1 = RemoteLocation('Основной')
        rem_loc1.receipt(print1, 100)

        store1 = Store("Центральный")

        trans1 = Transport("Газель")

        trans1.transfer(rem_loc1, store1, print1, 4)
        print(rem_loc1)
        print(rem_loc1.free_volume)
        print(store1)
        print(store1.free_volume)
        print("")

        trans1.transfer(rem_loc1, store1, print1, 4)
        print(rem_loc1)
        print(rem_loc1.free_volume)
        print(store1)
        print(store1.free_volume)
        print("")

        trans1.transfer(rem_loc1, store1, print1, 4)
        print(rem_loc1)
        print(rem_loc1.free_volume)
        print(store1)
        print(store1.free_volume)
        print("")

        trans1.transfer(rem_loc1, store1, print1, 6)
        print(rem_loc1)
        print(rem_loc1.free_volume)
        print(store1)
        print(store1.free_volume)
        print("")

    except OfficeEquipmentNotExistsError as e:
        print(e.txt)

    except LocationFullError as e:
        print(e.txt)



