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
    fabric_consumption_of_clothing = {
        'Coat': 0,
        'Suit': 0
    }

    def __init__(self, args):
        self.args = args
        self.FABRIC_CONSUMPTION_FORMULAS = {
            'Coat': f'{self.args / 6.5 + 0.5}',
            'Suit': f'{2 * self.args + 0.3}'
        }
        self.type_of_clothing = self.__class__.__name__
        self.__fabric_consumption = self.__getitem__()

    def __getitem__(self):
        try:
            return self.fabric_consumption_of_clothing[self.type_of_clothing]
        except KeyError:
            print('This type of clothing is not found')

    def __setitem__(self, value):
        self.fabric_consumption_of_clothing[self.type_of_clothing] += value

    @property
    def fabric_consumption(self):
        return self.__fabric_consumption

    @fabric_consumption.setter
    def fabric_consumption(self, value):
        self.__setitem__(value)

    def calculation_of_fabric_consumption(self):
        calc = float(self.FABRIC_CONSUMPTION_FORMULAS[self.type_of_clothing])
        self.fabric_consumption = calc
        return f'Fabric consumption for {self.type_of_clothing} ({self.args}): {calc:.2f}'


class Coat(Clothes):
    pass


class Suit(Clothes):
    pass


class ClothesDataInterface:
    @staticmethod
    def print_fabric_consumption():
        for key, value in Clothes.fabric_consumption_of_clothing.items():
            print(f'{key}: {value:.2f}')

    @staticmethod
    def calc_total():
        total = 0
        for value in Clothes.fabric_consumption_of_clothing.values():
            total += value
        return f'************\nTotal: {total:.2f}'


if __name__ == '__main__':
    coat1 = Coat(args=40)
    suit1 = Suit(args=1.60)
    print(coat1.calculation_of_fabric_consumption())
    print(suit1.calculation_of_fabric_consumption())
    print()
    coat2 = Coat(50)
    suit2 = Suit(1.80)
    print(coat2.calculation_of_fabric_consumption())
    print(suit2.calculation_of_fabric_consumption())
    print()
    clothes_data = ClothesDataInterface()
    clothes_data.print_fabric_consumption()
    print(clothes_data.calc_total())
