"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

inp_lines = []
with open("txt_tast1.txt", "w", encoding="UTF-8") as t_file:
    while True:
        item = input("Ведите строку файла: ")
        if item:
            inp_lines.append(f"{item}\n")
        else:
            break

    if len(inp_lines) > 0:
        t_file.writelines(inp_lines)



