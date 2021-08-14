"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной
схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        # return ''.join('  '.join(' ' * ((max([max(x) for x in [[len(str(x)) for x in self.matrix[i]] for i in range(len(self.matrix))]]) - len(str(self.matrix[i][j]))) // 2 + (max([max(x) for x in [[len(str(x)) for x in self.matrix[i]] for i in range(len(self.matrix))]]) - len(str(self.matrix[i][j]))) % 2) + str(self.matrix[i][j]) + ' ' * ((max([max(x) for x in [[len(str(x)) for x in self.matrix[i]] for i in range(len(self.matrix))]]) - len(str(self.matrix[i][j]))) // 2) if str(self.matrix[i][j])[0] != '-' else ' ' * ((max([max(x) for x in [[len(str(x)) for x in self.matrix[i]] for i in range(len(self.matrix))]]) - len(str(self.matrix[i][j]))) // 2) + str(self.matrix[i][j]) + ' ' * ((max([max(x) for x in [[len(str(x)) for x in self.matrix[i]] for i in range(len(self.matrix))]]) - len(str(self.matrix[i][j]))) // 2 + (max([max(x) for x in [[len(str(x)) for x in self.matrix[i]] for i in range(len(self.matrix))]]) - len(str(self.matrix[i][j]))) % 2) for j in range(len(self.matrix[i]))) + '\n' for i in range(len(self.matrix)))  # just kidding

        max_len = 1
        for line in self.matrix:
            for number in line:
                length = len(str(number))
                if length > max_len:
                    max_len = length
        # return ''.join('  '.join('{:>{max}}'.format(number, max=str(max_len)) for number in string) + '\n' for string in self.matrix)
        form = (('{:' + str(max_len) + '}  ') * len(self.matrix[0]))[:-2] + '\n'
        string = ''.join(form.format(*line) for line in self.matrix)
        return string

    def __add__(self, other):
        matrix_sum = []
        for i in range(len(self.matrix)):
            matrix_sum.append(list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i])))
        return Matrix(matrix_sum)


my_matrix_1 = [[1,  1,  1,  1],
               [1, -1,  1, -1],
               [1,  1, -1, -1],
               [1, -1, -1,  1]]

my_matrix_2 = [[-1,      -1, -1, -1],
               [-1,    -110, -1,  1],
               [-1,   11110,  1,  1],
               [-1,  100000,  1, -1]]

matrix_1 = Matrix(my_matrix_1)
matrix_2 = Matrix(my_matrix_2)
print(matrix_1)
print('+\n')
print(matrix_2)
new_matrix = matrix_1 + matrix_2
print('=\n')
print(new_matrix)
