"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_list: list):
        self._matrix_list = matrix_list
        self.rows = len(matrix_list)
        if self.rows:
            self.columns = len(self._matrix_list[0])


    def __getitem__(self, item) -> list :
        if item < len(self):
            return self._matrix_list[item]
        else:
            return []


    def __str__(self):
        return str(self._matrix_list)

    def __iter__(self):
        return Matrix_Iter(self)

    def __len__(self):
        return len(self._matrix_list)


    def __add__(self, other):
        matr = [[0 for row in range(0, max(len(matrix1), len(matrix2)))] for item in
                range(0, max(len(matrix1[0]), len(matrix2[0])))]

        row = 0
        for matr_row in matr:
            col = 0
            while col < len(matr_row):
                matr_row[col] += matrix1[row][col] if col < len(matrix1[row])  else 0
                matr_row[col] += matrix2[row][col] if col < len(matrix2[row]) else 0
                col += 1

            row +=1

        return Matrix(matr)



class Matrix_Iter:
    def __init__(self, matrix: Matrix):
        self._idx = -1
        self._matrix = matrix

    def __next__(self):
        self._idx += 1
        if self._idx < len(self._matrix):
            return self._matrix[self._idx]
        else:
            raise StopIteration



if __name__ == '__main__':

    matrix1 = Matrix([
        [1 , 4],
        [51, 20],
        [3, 20]
     ])

    print(matrix1)

    matrix2 = Matrix([
            [12 , 4, 61],
            [15, 29, 4]
         ])
    print(matrix2)

    print(matrix1 + matrix2)
