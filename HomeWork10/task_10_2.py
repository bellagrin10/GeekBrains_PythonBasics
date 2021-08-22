"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""


class Clothes:
    __fabric_consumption_of_clothing = {
        'Coat': 0,
        'Suit': 0
    }

    def __init__(self, args, total=0):
        self.args = args
        self.FABRIC_CONSUMPTION_FORMULAS = {
            'Coat': f'{self.args / 6.5 + 0.5}',
            'Suit': f'{2 * self.args + 0.3}'
        }
        self.type_of_clothing = self.__class__.__name__
        self.__fabric_consumption = self.__getitem__()
        self.__total = total

    @property
    def fabric_consumption(self):
        return self.__fabric_consumption

    def __getitem__(self):
        try:
            return self.__fabric_consumption_of_clothing[self.type_of_clothing]
        except KeyError:
            print('This type of clothing is not found')

    def __setitem__(self, value):
        self.__fabric_consumption_of_clothing[self.type_of_clothing] += value

    @fabric_consumption.setter
    def fabric_consumption(self, value):
        self.__setitem__(value)

    def print_fabric_consumption(self):
        for key, value in self.__fabric_consumption_of_clothing.items():
            print(f'{key}: {value:.2f}')

    @property
    def total(self):
        for value in self.__fabric_consumption_of_clothing.values():
            self.__total += value
        return f'Total: {self.__total:.2f}\n************'

    def calculation_of_fabric_consumption(self):
        calc = float(self.FABRIC_CONSUMPTION_FORMULAS[self.type_of_clothing])
        self.fabric_consumption = calc
        return f'Fabric consumption for {self.type_of_clothing} ({self.args}): {calc:.2f}'


class Coat(Clothes):
    pass


class Suit(Clothes):
    pass


if __name__ == '__main__':
    coat = Coat(args=40)
    suit = Suit(args=1.60)
    print(coat.calculation_of_fabric_consumption())
    print(suit.calculation_of_fabric_consumption())
    print()
    coat1 = Coat(50)
    suit1 = Suit(1.80)
    print(coat1.calculation_of_fabric_consumption())
    print(suit1.calculation_of_fabric_consumption())
    print()
    print(coat.total)
    coat.print_fabric_consumption()
