"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его
работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDev(Exception):

    def __init__(self, txt="Сan't divide it by zero"):
        self.txt = txt


try:
    n1 = int(input('Enter a divisible: '))
    n2 = int(input('Enter a divisor: '))
    if n2 == 0:
        raise ZeroDev("Сan't divide it by zero")
    quotient = n1 / n2
    print('Quotient:', int(quotient) if quotient == n1 // n2 else quotient)
except ZeroDev as e:
    print(e)
except ValueError as e:
    print('Error:', e)
