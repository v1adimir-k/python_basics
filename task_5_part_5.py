"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('test_file_for_part_5.txt', 'w') as f:
    f.write('1 2 3 4 5 6 7 8 9')

with open('test_file_for_part_5.txt') as f:
    data = [int(number) for number in f.read().split()]
    print(sum(data))
