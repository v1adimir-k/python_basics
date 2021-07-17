import shutil
from random import randint

# Часть 1
# =====================================================================================================================
print('Часть №1')
print('='*(shutil.get_terminal_size()[0]-1))
integer_var = 5
float_var = 5.1
string_var = 'text'
wtf_var = eval("[{!r}, {!r}, {!r}, {!r}, {}]".format("This", "is", "list", "no.", int(1.0)))
print('Созданы несколько переменных:')
print(f'1. {integer_var}, type: {type(integer_var)}')
print(f'2. {float_var}, type: {type(float_var)}')
print(f'3. {string_var}, type: {type(string_var)}')
print(f'4. {wtf_var}, type: {type(wtf_var)}')

print('\nЗадайте свои переменные')
while True:
    try:
        integer_var_new = int(input('Введите целое число: '))
        float_var_new = float(input('Введите число с плавающей точкой: ').replace(',', '.'))
        string_var_new = str(input('Введите строку: '))
        break
    except ValueError:
        print('\nПопробуйте заново и введите что требуется')

print('\nВаши переменные:')
print(f'1. {integer_var_new}, type: {type(integer_var_new)}')
print(f'2. {float_var_new}, type: {type(float_var_new)}')
print(f'3. {string_var_new}, type: {type(string_var_new)}')

print('\nНажмите любую клавишу, чтобы продолжить ...')
input()

# Часть 2
# =====================================================================================================================
print('\nЧасть №2')
print('='*(shutil.get_terminal_size()[0]-1))
seconds = int(input('Введите время в секудндах: '))

print(f"Время здорового человека: "
      f"{seconds//(60*60):02}:{seconds%(60*60)//60:02}:{seconds%(60*60)%60:02}")

print('\nНажмите любую клавишу, чтобы продолжить ...')
input()

# Часть 3
# =====================================================================================================================
print('\nЧасть №3')
print('='*(shutil.get_terminal_size()[0]-1))
n = input('Введите число: ')
n_nn_nnn = [int(n), int(n*2), int(n*3)]
print('{} + {} + {} = {}'.format(*n_nn_nnn, sum(n_nn_nnn)))

print('\nНажмите любую клавишу, чтобы продолжить ...')
input()

# Часть 4
# =====================================================================================================================
print('\nЧасть №4')
print('='*(shutil.get_terminal_size()[0]-1))
number = input('Введите целое положительно число: ')

random_choice = randint(0, 1)
if random_choice == 1:  # нормальный вариант
    number_by_digits = list(number)
    number_by_digits.sort(reverse=True)
    biggest_digit = number_by_digits[0]
else:  # вариант с цикллом while и арифметическими операциями...
    i = 1
    biggest_digit = number[0]
    while i < len(number):
        if biggest_digit < number[i]:
            biggest_digit = number[i]
        i += 1

print('Наибольшая цифра:', biggest_digit)
print('\nНажмите любую клавишу, чтобы продолжить ...')
input()

# Часть 5
# =====================================================================================================================
print('\nЧасть №5')
print('='*(shutil.get_terminal_size()[0]-1))
revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if revenue > costs:
    print('\nВаша фирма прибыльна')
    print('Рентабельность выручки:', round((revenue-costs)/revenue, 3))
    number_of_employees = int(input('Введите кол-во сотрудников в вашей фирме: '))
    print('Прибыль в расчете на одного содтрудника:', round((revenue-costs)/number_of_employees, 1))
elif revenue < costs:
    print('\nВаша фирма убыточна')
else:
    print('\nВыручка равна издержкам')

print('\nНажмите любую клавишу, чтобы продолжить ...')
input()

# Часть 6
# =====================================================================================================================
print('\nЧасть №6')
print('='*(shutil.get_terminal_size()[0]-1))
result = int(input('Введите, сколько спортсмен пробежал в первый день: '))
goal = int(input('Желаемый результат для спортсмена (в километрах): '))

predicted_result = result
day_of_predicted_result = 1
while predicted_result < goal:
    predicted_result = round(predicted_result*1.1, 2)
    day_of_predicted_result += 1

if day_of_predicted_result < 5:
    print(f'Потребуется {day_of_predicted_result} дня')
else:
    print(f'Потребуется {day_of_predicted_result} дней')

print('\nThe End')
input()
