"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""


def my_func(a, b, c):
    list_1 = [a, b, c]
    list_1.sort(reverse=True)
    return sum(list_1[:2])


while True:
    try:
        number_1 = int(input('Введите число: '))
        number_2 = int(input('Введите еще одно число: '))
        number_3 = int(input('И еще разок : '))

        result = my_func(number_1, number_2, number_3)
        print(f'Сумма наибольших чисел: {result}\n')
    except ValueError:
        print('\nНеобходимо вводить число, попробуйте заново!')
