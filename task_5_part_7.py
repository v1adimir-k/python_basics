"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

with open('test_file_for_part_7.txt', 'r', encoding='utf-8-sig') as f:
    data = [line.split() for line in f.readlines()]

profits = {}
losses = {}
sum_of_profits = 0
for i in range(len(data)):
    diff = int(data[i][2]) - int(data[i][3])
    if diff >= 0:
        profits[data[i][0]] = diff
        sum_of_profits += diff
    else:
        losses[data[i][0]] = diff

result = [profits, {'average_profit': int(sum_of_profits / len(data))}, losses]
print(result)

with open('test_file_for_part_7.json', 'w') as f:
    json.dump(result, f)
