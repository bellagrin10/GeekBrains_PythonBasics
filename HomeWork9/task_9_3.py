"""
Реализовать базовый класс Worker (работник):
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
  например, {"wage": wage, "bonus": bonus};
- создать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
  дохода с учётом премии (get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
  проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self._income


class Position(Worker):
    def __init__(self, *args):
        super().__init__(*args)

    def get_full_name(self):
        return f'employee name: {self.name} {self.surname}'

    def get_total_income(self):
        income = self.get_income()
        total_income = income["wage"] * 12 + income["bonus"]
        return f'his income: {total_income}'


pos1 = Position('Sherlock', 'Holmes', 'detective', 20000, 1000)
print(pos1.get_full_name(), pos1.get_total_income(), sep='\n')
pos2 = Position('John', 'Watson', 'doctor', 10000, 500)
print(pos2.get_full_name(), pos2.get_total_income(), sep='\n')
pos3 = Position('Athelney', 'Jones', 'police inspector', 3000, 100)
print(pos3.__dict__)
