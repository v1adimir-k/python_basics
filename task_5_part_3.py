"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

with open('test_file_for_part_3.txt', 'r', encoding='utf-8-sig') as f:
    data = [data.split() for data in f.readlines()]

print('Сотрудники, с окладом менее 20 тыс.:')
total = 0
for i in range(len(data)):
    amount = int(data[i][1])
    if amount < 20000:
        print(data[i][0][:-1])
    total += amount

print('\nСредняя величина дохода:\n', int(total / len(data)), sep='')
