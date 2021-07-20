"""
Given a list containing garbled data with positions and names of employees.
It is known that an employee's name is always at the end of a line.
Form from these names and display phrases of the form: 'Hello, Igor!'
"""

data_of_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                     'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i, data in enumerate(data_of_employees):
    *position, name = data.split()[:-1], data.split()[-1].title()
    data_of_employees[i] = ' '.join(*position), name
    print(f'Привет, {data_of_employees[i][1]}!')
