"""
Реализовать класс Road (дорога).
- определить атрибуты: length (длина), width (ширина);
- значения атрибутов должны передаваться при создании экземпляра класса;
- атрибуты сделать защищёнными;
- определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
- использовать формулу:
  длина * ширина * масса асфальта для покрытия одного кв.м. дороги асфальтом, толщиной в 1см * число см толщины полотна;
проверить работу метода.

Например: 20 м * 5000 м * 25 кг * 5 см = 12500 т.
"""


class Road:
    MASS_PER_SQ_M_PER_CM_THICK = 25

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calc_the_required_mass_of_asphalt(self, thickness):
        result = self._width * self._length * Road.MASS_PER_SQ_M_PER_CM_THICK * thickness
        return f'The mass of asphalt required to cover the entire road:\n{result / 1000} т.'


road = Road(5000, 20)

# set the thickness of the road bed in cm
road.calc_the_required_mass_of_asphalt(5)
print(road.calc_the_required_mass_of_asphalt(5))
