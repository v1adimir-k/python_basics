"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в
степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование
цикла.
"""
from random import randint


def nice(n):
    return n if not str(n).endswith(".0") else int(n)


def my_func(x, y):
    print(f'{nice(x)}^{nice(y)} =', nice(x**y))


def my_func_2(x, y):
    z = x
    for i in range(1, abs(y)):
        z *= x
    print(f'{nice(x)}^{nice(y)} =', nice(1 / z))


while True:
    try:
        number_1 = float(input('Введите действительное положительное число: '))
        if number_1 != abs(number_1):
            print('Число должно быть положительное!')
            continue
        number_2 = int(input('Введите целое отрицательное число: '))
        if number_2 == abs(number_2):
            print('Число должно быть отрицательное!')
            continue
        if randint(0, 1) == 1:
            my_func(number_1, number_2)
        else:
            my_func_2(number_1, number_2)
    except ValueError:
        print('Необходимо ввести требуемое число!')
    finally:
        print()
