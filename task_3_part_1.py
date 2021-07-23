"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(a, b):
    try:
        c = round(a / b, 3)
        if str(c).endswith('.0'):
            c = int(c)
        print('Результат:', c)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


while True:
    try:
        number_1 = float(input('Введите делимое: ').replace(",", ''))
        number_2 = float(input('Введите делитель: ').replace(",", ''))
        divide(number_1, number_2)
    except ValueError:
        print('Необходимо ввести число!')
    finally:
        print()
