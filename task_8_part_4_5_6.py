"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
from datetime import datetime


class Warehouse:
    free_space = 20
    stored = {}  # {'eq_type': {'model': {'amount': 0, 'log': []}}, ...}
    sent = {}  # {'dept': {'eq_type': {'model': {'amount': 0, 'log': []}}, ...}, ...}

    @classmethod
    def store(cls, eq_type, model, amount):
        if cls.free_space >= amount:
            if not cls.stored.get(eq_type):
                cls.stored[eq_type] = {}
            if not cls.stored[eq_type].get(model):
                cls.stored[eq_type][model] = {'amount': 0, 'log': []}
            cls.stored[eq_type][model]['amount'] += amount
            cls.stored[eq_type][model]['log'].append((amount, '{:%H:%M:%S %d.%m.%Y}'.format(datetime.today())))
            cls.free_space -= amount
            print('Добавлено на склад. Свободных мест осталось:', cls.free_space)
        else:
            raise Exception(f'Недостаточно свободных мест. Доступно мест: {cls.free_space}')

    @classmethod
    def send(cls, dep, eq_type, model, amount):
        if cls.stored.get(eq_type) and cls.stored[eq_type].get(model) and cls.stored[eq_type][model]['amount'] >= amount:
            if not cls.sent.get(dep):
                cls.sent[dep] = {}
            if not cls.sent[dep].get(eq_type):
                cls.sent[dep][eq_type] = {}
            if not cls.sent[dep][eq_type].get(model):
                cls.sent[dep][eq_type][model] = {'amount': 0, 'log': []}
            cls.stored[eq_type][model]['amount'] -= amount
            cls.sent[dep][eq_type][model]['amount'] += amount
            cls.sent[dep][eq_type][model]['log'].append((amount, '{:%H:%M:%S %d.%m.%Y}'.format(datetime.today())))
            print('Отправлено')
        elif not cls.stored.get(eq_type):
            raise Exception(f'Нету необходимого кол-ва на складе, доступно "{eq_type}": {cls.stored.get(eq_type)}')
        elif not cls.stored[eq_type].get(model):
            raise Exception(f'Нету необходимого кол-ва на складе, доступно "{eq_type} {model}": {cls.stored[eq_type].get(model)}')


class OfficeEquipment:
    budget = 50000

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def buy(self, amount):
        available = OfficeEquipment.budget // self.price
        if available >= amount:
            try:
                eq_type = str(self.__class__)
                eq_type = eq_type[eq_type.find('.')+1:-2].lower()
                Warehouse.store(eq_type, self.model, amount)
                OfficeEquipment.budget -= amount * self.price
            except Exception as e:
                print(e)
        else:
            print('Недостаточно средств.')

    @property
    def available(self):
        return int(OfficeEquipment.budget // self.price)

    def __str__(self):
        return 'Модель: {}, Цена: {}, Особенности: {}'.format(self.model, self.price, str(self.features)[
                1:-1].replace("'", ''))


class Printer(OfficeEquipment):

    def __init__(self, model, price, features):
        super().__init__(model, price)
        self.features = features


class Scanner(OfficeEquipment):

    def __init__(self, model, price, features):
        super().__init__(model, price)
        self.features = features


class Copier(OfficeEquipment):

    def __init__(self, model, price, features):
        super().__init__(model, price)
        self.features = features


def main():
    equipment = []
    count = 1
    while True:
        try:
            print('Выберете вариант и введите соответствующую цифру:\n'
                  '1. Создать вариант оборудования\n'
                  '2. Закупить оборудование и добавить на склад\n'
                  '3. Узнать, сколько оборудования можно купить\n'
                  '4. Посмотреть и изменить бюджет\n'
                  '5. Отправить оборудование со склада в отдел\n'
                  '6. Узнать наличие оборудования на складе\n'
                  '7. Посмотреть список сохраненных вариантов оборудования\n'
                  '8. Отобразить описание сохраненного варианта оборудования')
            choice = input('>>> ')
            print()
            if choice == '1':
                eq_type = input('Введите "printer", "copier" или "scanner": ')
                if eq_type not in ('printer', 'copier', 'scanner'):
                    raise Exception('Такое оборудование недоступно.')
                model = input('Введите название модели: ')
                if not model:
                    raise Exception('Название модели не может быть пустым.')
                price = int(input('Введите цену данной модели: '))
                if not price:
                    raise Exception('Необходимо указать цену.')
                print('Введите через запятую c пробелом ", " характеристики данной модели, если считаете нужным:')
                features = input('>>> ').split(', ')
                obj = f'{eq_type}_id{count}'
                exec(f'{obj} = {eq_type.capitalize()}("{model}", {price}, {features})')
                equipment.append(obj)
                print(f'Вы сохранили вариант оборудования с id={count}, он будет доступен, как "{obj}".\n')
                count += 1

            elif choice == '2':
                model = input('Введите название сохарненного оборудования: ')
                if model not in equipment:
                    raise Exception('Нету такого варианта оборудования')
                amount = int(input('Введите, какое кол-во данного оборудования хотите закупить: '))
                print()
                exec(f'{model}.buy({amount})')

            elif choice == '3':
                model = input('Введите название сохарненного оборудования: ')
                if model not in equipment:
                    raise Exception('Нету такого варианта оборудования')
                amount = eval(f'{model}.available')
                print(f'Доступно: {amount}\n')

            elif choice == '4':
                print('Текущий бюджет:', OfficeEquipment.budget)
                print('Хотите увеличить бюджет? Введите "да":')
                ch = input('>>> ')
                if ch == "да":
                    amount = int(input('Введите кол-во: '))
                    OfficeEquipment.budget += amount
                    print('Текущий бюджет:', OfficeEquipment.budget)
                    print()

            elif choice == '5':
                dept = input('Введите название отдела, куда хотите отправить: ')
                eq_type = input('Введите тип оборудования: ')
                model = input('Введите модель: ')
                amount = int(input('Введите кол-во: '))
                Warehouse.send(dept, eq_type, model, amount)
                print()

            elif choice == '6':
                eq_type = input('Введите тип оборудования: ')
                model = input('Введите модель: ')
                print(f'Доступно: {Warehouse.stored[eq_type][model]["amount"]}\n')

            elif choice == '7':
                equipment.sort()
                print(f'{equipment}\n')

            elif choice == '8':
                model = input('Введите название сохарненного оборудования: ')
                if model not in equipment:
                    raise Exception('Нету такого варианта оборудования')
                print(eval(model))
                print()
            print()
        except ValueError as e:
            print('Необходимо задать численное значение\n\n')
        except Exception as e:
            print(f'{e}\n\n')


if __name__ == "__main__":
    main()
