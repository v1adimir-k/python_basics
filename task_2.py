import shutil
from random import randint

# Часть 1
# =================================================================================================
"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки
типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно
не запрашивать у пользователя, а указать явно, в программе.
"""
print('Часть №1')
print('='*(shutil.get_terminal_size()[0]-1))

my_list = [1, 1.2, 'string', True, b'\xff', ['list', 1], ('tuple', 1), {'set', 1}, {'dict': 1}]
for i in range(len(my_list)):
    print(f'{i+1}. {my_list[i]}, {type(my_list[i])}')

print('\nНажмите любую клавишу, чтобы продолжить ...')
input()

# Часть 2
# =================================================================================================
"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы 
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем 
месте. Для заполнения списка элементов необходимо использовать функцию input().
"""
print('Часть №2')
print('='*(shutil.get_terminal_size()[0]-1))

while True:
    print('Введите элементы списка через пробел:')
    list_1 = input('>>> ').split()

    i = 1
    while i < len(list_1):
        list_1[i - 1], list_1[i] = list_1[i], list_1[i - 1]
        i += 2
    print('\nИзмененный список:\n', list_1, sep='')

    print('\nНажмите Enter, чтобы продолжить, или введите "+", чтобы повторить часть №2')
    if not input():
        break
    print()

# Часть 3
# =================================================================================================
"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года 
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
print('Часть №3')
print('='*(shutil.get_terminal_size()[0]-1))

while True:
    month = int(input('Введите номер месяца: '))
    random_choice = randint(0, 1)
    if random_choice == 1:
        my_list = [['зима', (12, 1, 2)], ['весна', (3, 4, 5)],
                   ['лето', (6, 7, 8)], ['осень',  (9, 10, 11)]]
        for i in range(len(my_list)):
            if month in my_list[i][1]:
                print(f'Это {my_list[i][0][:-1]}ний месяц')
                break
            elif i == len(my_list) - 1:
                print('Нету такого месяца')
    else:
        my_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
        ch = None
        for key, value in my_dict.items():
            if month in value:
                print(f'Это {key[:-1]}ний месяц')
                ch = 1
                break
        if ch is None:
            print('Нету такого месяца')

    print('\nНажмите Enter, чтобы продолжить, или введите "+", чтобы повторить часть №3')
    if not input():
        break
    print()

# Часть 4
# =================================================================================================
"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с 
новой строки. Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 
букв в слове.
"""
print('Часть №4')
print('='*(shutil.get_terminal_size()[0]-1))

while True:
    input_list = input('Введите слова через пробел: ').split()
    for i in range(len(input_list)):
        print(f'{i+1}. {input_list[i][:10]}')

    print('\nНажмите Enter, чтобы продолжить, или введите "+", чтобы повторить часть №4')
    if not input():
        break
    print()

# Часть 5
# =================================================================================================
"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы 
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
print('Часть №5')
print('='*(shutil.get_terminal_size()[0]-1))

rate_list = []
while True:
    print('Введите натуральное число, чтобы добавить его в рейтинг, '
          'или нажмите Enter, чтобы выйти')
    number = input('>>> ')
    if number == '':
        print()
        break
    elif number.isdigit() and number != '0':
        number = int(number)
    else:
        print('\nПопробуйте снова...')
        continue
    rate_list.append(int(number))
    rate_list.sort(reverse=True)
    print(f'Рейтинг: {str(rate_list)[1:-1]}\n')

# Часть 6
# =================================================================================================
"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый 
кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и 
словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — 
характеристика товара, например название, а значение — список значений-характеристик, 
например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
print('Часть №6')
print('='*(shutil.get_terminal_size()[0]-1))

while True:
    print('Желаете задать параметры товаров, которые будут заноситься в базу данных? Введите '
          '"да", чтобы задать параметры или "нет", чтобы использовать параметры по умолчанию:')
    set_choice = input('>>> ').replace('"', '')
    if set_choice == 'да':
        print('\nВведите через запятую и пробел ", " параметры товаров, '
              'например: "название", "цена", "количество" и тп.')
        parameters = input('>>> ').replace('"', '').split(', ')
    else:
        parameters = ['название', 'цена', 'количество', 'ед']

    products = []
    while True:
        print('\nВведите "+", чтобы добавить информацию о товаре в базу данных, '
              'или нажмиите Enter, чтобы завершить добавление товаров')
        choice = input('>>> ')
        if choice == '':
            break
        product = {}
        for item in parameters:
            value = input(f'{item}: ')
            product[item] = int(value) if value.isdigit() else value
        products.append(((len(products)+1), product))

    product_analysis = {}
    for parameter in parameters:
        product_analysis.setdefault(parameter, [])
        for i in range(len(products)):
            if products[i][1][parameter] not in product_analysis[parameter]:
                product_analysis[parameter].append(products[i][1][parameter])

    print('\nАналитика по товарам:')
    for key, value in product_analysis.items():
        print(f'''{key}: {str(value)[1:-1].replace("'","")}''')

    print('\nКонец. Нажмите Enter, чтобы выйти, или введите "+", чтобы повторить часть №6')
    if not input():
        break
    print()
