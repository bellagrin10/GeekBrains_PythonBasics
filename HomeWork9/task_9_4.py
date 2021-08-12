"""
Реализуйте базовый класс Car:
_ у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
  go, stop, turn (direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed.
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, new_speed):
        self.speed = new_speed
        print(f'The {self.color} {self.name} is moving at a speed {self.speed} km.h.')

    def stop(self):
        self.speed = 0
        print(f'The {self.color} {self.name} stopped.')

    def turn(self, direction):
        self.speed -= 20
        print(f'The {self.color} {self.name} turned {direction}.')

    def show_speed(self):
        print(f'Speed: {self.speed}')


class TownCar(Car):
    def __init__(self, *args):
        super().__init__(*args)
        self.length = 5.49
        self.wheel_drive = 'rear'

    def show_speed(self):
        super().show_speed() if self.speed <= 60 else print('OVER SPEED!!')


class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)
        self.weight = 2275


class WorkCar(Car):
    def __init__(self, *args, type_):
        super().__init__(*args)
        self.type = type_

    def show_speed(self):
        super().show_speed() if self.speed <= 40 else print('OVER SPEED!!')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args)
        self.is_police = True
        self.is_siren = True
        self.is_flashing_lights = True

    def go(self, new_speed):
        super().go(new_speed)
        print(f'SIREN!!! and ***FLASHER*** works.')


car = Car(200, 'white', 'Audi')
print(car.__dict__)
town_car = TownCar(180, 'blue', 'Cadillac')
print(town_car.name, town_car.color, town_car.length, town_car.wheel_drive)
sport_car = SportCar(400, 'red', 'Toyota')
print(sport_car.speed, sport_car.color, sport_car.weight)
work_car1 = WorkCar(130, 'green', 'Honda Hunter', type_='truck')
print(work_car1.name, work_car1.type)
work_car2 = WorkCar(120, 'yellow', 'Ford Transit', type_='van')
print(work_car2.name, work_car2.type)
police_car = PoliceCar(300, 'black', 'Police')
print(police_car.is_police, police_car.speed, police_car.is_siren, police_car.is_flashing_lights)

town_car.go(65)
town_car.show_speed()
town_car.turn('left')
town_car.show_speed()
town_car.stop()
town_car.show_speed()

police_car.go(160)
police_car.show_speed()
police_car.turn('right')
police_car.show_speed()
police_car.go(180)
police_car.turn('left')
police_car.show_speed()
police_car.stop()
police_car.show_speed()
