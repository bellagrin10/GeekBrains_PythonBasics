"""
Реализовать проект «Операции с комплексными числами».
Создать класс «Комплексное число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
"""


class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real}{self.imaginary:+d}i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        """
        Формула умножения комплексных чисел: (x+yi)(u+vi) = (xu-yv) + (xv+yu)i
        """
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)


complex1 = Complex(3, 2)
print('complex1: ', complex1)
complex2 = Complex(1, 4)
print('complex2: ', complex2)
complex3 = Complex(5, -3)
print('complex3: ', complex3)

print('complex1 + complex2: ', complex1 + complex2)
print('complex1 + complex3: ', complex1 + complex3)
print('complex1 * complex2: ', complex1 * complex2)
print('complex1 * complex3: ', complex1 * complex3)
