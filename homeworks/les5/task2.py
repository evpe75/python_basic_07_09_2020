"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

dict_lines = {}
with open("text_task2.txt", "r", encoding="UTF-8") as read_file:
    for idx, item in enumerate(read_file):
        dict_lines[idx+1] = len(str(item).split(" "))

print(dict_lines)
