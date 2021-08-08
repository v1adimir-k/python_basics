"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что
машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При
значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            return True
        else:
            return False

    def stop(self):
        if self.speed == 0:
            return True
        else:
            return False

    def turn(self, direction='-'):
        if direction == 'right' or direction == 'left':
            return direction
        else:
            return direction

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} - Speeding!'
        else:
            return self.speed


class SportCar(Car):

    def state(self):
        if self.speed > 120:
            return 'wants to get some problems'


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} - Speeding!'
        else:
            return self.speed


class PoliceCar(Car):

    def state(self):
        if self.speed > 120:
            return 'chasing someone'


town_car = TownCar(0, 'white', 'Toyota', False)
print('Town Car')
print('Car color:', town_car.color)
print('Car name:', town_car.name)
print('Is police:', town_car.is_police)
print('Is moving:', town_car.go())
print('Is stopped:', town_car.stop())
print('Car turned:', town_car.turn())
print('Speed:', town_car.show_speed())
print()


sport_car = SportCar(150, 'red', 'Ferrari', False)
print('Sport Car')
print('Car color:', sport_car.color)
print('Car name:', sport_car.name)
print('Is police:', sport_car.is_police)
print('Is moving:', sport_car.go())
print('Is stopped:', sport_car.stop())
print('Car turned:', sport_car.turn())
print('Speed:', sport_car.show_speed())
print('State:', sport_car.state())
print()


work_car = WorkCar(50, 'yellow', 'Ford', False)
print('Work Car')
print('Car color:', work_car.color)
print('Car name:', work_car.name)
print('Is police:', work_car.is_police)
print('Is moving:', work_car.go())
print('Is stopped:', work_car.stop())
print('Car turned:', work_car.turn('right'))
print('Speed:', work_car.show_speed())
print()


police_car = PoliceCar(150, 'black', 'Dodge', True)
print('Police Car')
print('Car color:', police_car.color)
print('Car name:', police_car.name)
print('Is police:', police_car.is_police)
print('Is moving:', police_car.go())
print('Is stopped:', police_car.stop())
print('Car turned:', police_car.turn())
print('Speed:', police_car.show_speed())
print('State:', police_car.state())
print()
