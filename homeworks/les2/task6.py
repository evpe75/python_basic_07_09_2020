"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и
словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

input_value = None

print("Начинаем заполнение каталога товаров")
idx = 0
item_list = []

while input_value != "N":

    if input_value is None:
        input_value = "Y"
    else:
        input_value = input("Есть еще номенклатуры в каталоге? (Y/N): ")

    if input_value != "Y" and input_value != "N":
        print("Введена неверная команда, попробуйте еще раз")
    elif input_value == "Y":
        idx += 1
        item_dict = dict([])

        item_dict['Name'] = input("Введите наименование товара: ")

        input_value = None

        while (input_value is None or not input_value.isdigit()):
            if not input_value is None:
                print("Введено не целое число, попробуйте еще раз")

            input_value = input("Введите цену товара в виде целого числа: ")

        item_dict["Price"] = int(input_value)

        input_value = None

        while (input_value is None or not input_value.isdigit()):
            if not input_value is None:
                print("Введено не целое число, попробуйте еще раз")

            input_value = input("Введите количество товара в виде целого числа: ")

        item_dict["Count"] = int(input_value)

        item_dict['UnitOfMeasure'] = input("Введите единицу измерения товара: ")

        item_list.append((idx, item_dict))

print(item_list)

