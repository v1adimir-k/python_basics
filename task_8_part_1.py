"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от
1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def number(cls, the_date):
        try:
            return [int(x) for x in the_date.split('-')]
        except Exception as e:
            return f'Ошибка: {e}'

    @staticmethod
    def valid(the_date):
        numbers = [int(x) for x in the_date.split('-')]
        if numbers[0] not in range(1, 32):
            return 'Invalid date, there are only 31 days in a month.'
        elif numbers[1] == 2 and numbers[0] not in range(1, 29) and numbers[2] % 4:
            return 'Invalid date, there are only 28 days in this month.'
        elif numbers[1] == 2 and numbers[0] not in range(1, 30) and not numbers[2] % 4:
            return 'Invalid date, there are only 29 days in this month.'
        elif numbers[1] not in range(1, 13):
            return 'Invalid date, there are only 12 month in a year.'
        elif len(str(numbers[2])) < 4:
            return 'Invalid date, please enter the year in four-digit format.'
        return 'The date is correct.'


date_1 = Date('30-02-2020')
print(Date.number(date_1.date))
print(Date.valid(date_1.date))
