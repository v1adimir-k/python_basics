"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
(класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом
проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и
рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу
декоратора @property.
"""
from abc import ABC, abstractmethod
from math import ceil


class Clothes(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):

    @property
    def fabric(self):
        return self.value / 6.5 + 0.5


class Suit(Clothes):

    @property
    def fabric(self):
        return 2 * self.value + 0.3


coat_1 = Coat(50)
print(f'Fabric amount for cloth 1: {ceil(coat_1.fabric)}')

suit_1 = Suit(180)
print(f'Fabric amount for suit 1: {ceil(suit_1.fabric)}')

print(f'Total fabric amount: {ceil(coat_1.fabric + suit_1.fabric)}')
