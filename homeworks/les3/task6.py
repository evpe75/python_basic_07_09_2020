"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

def int_func(str_lower: str) -> str:
    return str_lower[0].upper() + str_lower[1:]

print(int_func(input("Введите слово из маленьких латинских букв: ")))