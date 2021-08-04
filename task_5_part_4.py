"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
"""

words = [['One', 'Один'], ['Two', 'Два'], ['Three', 'Три'], ['Four', 'Четыре'], ['Five', 'Пять'],
         ['Six', 'Шесть'], ['Seven', 'Семь'], ['Eight', 'Восемь'], ['Nine', 'Девять']]

with open('test_file_for_part_4.txt', 'r', encoding='utf-8-sig') as f1:
    data = f1.readlines()

for i in range(len(data)):
    for j in range(len(words)):
        if data[i].startswith(words[j][0]):
            data[i] = data[i].replace(words[j][0], words[j][1])

with open('test_file_for_part_4_new.txt', 'w', encoding='utf-8-sig') as f2:
    f2.writelines(data)

print('Done')
