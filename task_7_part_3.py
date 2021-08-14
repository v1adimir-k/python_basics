"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий ячеек клетки (целое число). В классе
должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны
применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество
ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.
"""


class Cell:

    def __init__(self, number_of_units):
        self.number_of_units = number_of_units

    def __add__(self, other):
        return Cell(self.number_of_units + other.number_of_units)

    def __sub__(self, other):
        diff = self.number_of_units - other.number_of_units
        if diff > 0:
            return Cell(diff)
        else:
            raise Exception('The difference is negative')

    def __mul__(self, other):
        return Cell(self.number_of_units * other.number_of_units)

    def __truediv__(self, other):
        return Cell(self.number_of_units // other.number_of_units)

    def make_order(self, number_of_units_in_a_row):
        return ('*' * number_of_units_in_a_row + '\n') * (self.number_of_units // number_of_units_in_a_row) \
               + '*' * (self.number_of_units % number_of_units_in_a_row)


cell_1 = Cell(10)
cell_2 = Cell(15)
print(f'Sum: {(cell_1 + cell_2).number_of_units}')
try:
    print(f'Difference: {(cell_1 - cell_2).number_of_units}')
except Exception as e:
    print(e)
print(f'Product: {(cell_1 * cell_2).number_of_units}')
print(f'Division: {(cell_1 / cell_2).number_of_units}\n')


print(cell_1.make_order(4))
