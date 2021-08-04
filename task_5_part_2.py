"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке.
"""

with open('test_file_for_part_2.txt', 'r', encoding='utf-8-sig') as f:
    file_data = f.readlines()

for i in range(len(file_data)):
    file_data[i] = file_data[i].split()
    j = 0
    while j < len(file_data[i]):
        if set(file_data[i][j]).issubset(r'1234567890~`!@#№$%^&*()_-—+=<>{}[]:;"?.,\/'):
            del file_data[i][j]
        j += 1

print('Всего строк:', len(file_data))
print('Символов в каждой строке:')
for i, data in enumerate(file_data, 1):
    print(f'{i}: {len(data)}')

