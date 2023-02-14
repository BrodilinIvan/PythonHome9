"""Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

import copy
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)

    def __str__(self):
        st = ''
        for i in range(len(self.matrix)):
            st = st + '\t'.join(map(str, self.matrix[i])) + '\n'
        return st


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mx1 = Matrix(m1)
mx2 = Matrix(m2)
rezult = mx1 + mx2
print(mx1)
print(mx2)
print(rezult)


