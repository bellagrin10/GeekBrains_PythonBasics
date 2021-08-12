"""
Создать класс TrafficLight (светофор):
- определить у него один атрибут color (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
  третьего (зелёный) — на ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    def __init__(self, interval):
        self.__color = ['red', 'yellow', 'green']
        self.index_ = 0
        self.duration = [7, 2, interval]

    def running(self, num_of_switching):
        start = self.index_
        end = start + num_of_switching
        print('Traffic light in action:')
        for color in range(start, end):
            self.index_ = color % 3
            print(self.__color[self.index_])
            time.sleep(self.duration[self.index_])
        self.index_ += 1


# задать продолжительность третьего состояния (зелёный)
light = TrafficLight(3)

# задать количество переключений светофора
light.running(2)
light.running(4)
light.running(1)
