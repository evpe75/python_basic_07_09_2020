"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

rus_dict = {1: "Один",
            2: "Два",
            3: "Три",
            4: "Четыре"}

with open("text_task4.txt", "r", encoding="UTF-8") as eng_list:
    eng_items = {int(str(item).split(" — ")[1]) : str(item).split(" — ")[0] for item in eng_list}

with open("rus_text_task4.txt", "w", encoding="UTF-8") as rus_list:
    for idx, item in eng_items.items():
        rus_list.write(f"{rus_dict[idx]} — {idx}\n")
