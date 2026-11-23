'''
В следующих заданиях требуется реализовать абстрактный базовый класс,
определив в нем абстрактные методы и свойства.
Эти методы определяются в производных классах.
Для ввода использовать вспомогательный класс Reader,
позволяющий читать данные с клавиатуры.
Для вывода использовать методы __str__ или __repr__.
Вызывающая программа должна продемонстрировать все варианты вызова
переопределенных абстрактных методов.
Написать функцию вывода, получающую параметры базового класса
по ссылке и демонстрирующую виртуальный вызов.

Вариант 9. Создать абстрактный базовый класс Pair
с виртуальными арифметическими операциями.
Реализовать производные классы Complex (комплексное число)
и Rational (рациональное число).
'''
from abc import ABC, abstractmethod
from math import gcd

class Reader:
    @staticmethod
    def read_float(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка! Введите корректное число.")

    @staticmethod
    def read_int(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка! Введите корректное целое число.")

class Pair(ABC):
    def __init__(self, first: float, second: float):
        self._first = first
        self._second = second

    @property
    @abstractmethod
    def first(self):
        pass

    @property
    @abstractmethod
    def second(self):
        pass
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    # Абстрактные методы для вывода
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class Complex(Pair):
    def __init__(self, real: float, imag: float):
        super().__init__(real, imag)

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second
    def __add__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.first + other.first, self.second + other.second)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.first - other.first, self.second - other.second)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = self.first * other.first - self.second * other.second
        imag_part = self.first * other.second + self.second * other.first
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        denominator = other.first ** 2 + other.second ** 2
        if denominator == 0:
            raise ZeroDivisionError("Деление на ноль!")
        real_part = (self.first * other.first + self.second * other.second) / denominator
        imag_part = (self.second * other.first - self.first * other.second) / denominator
        return Complex(real_part, imag_part)

    def __str__(self):
        sign = "+" if self.second >= 0 else "-"
        return f"({self.first} {sign} {abs(self.second)}i)"

    def __repr__(self):
        return f"Complex({self.first}, {self.second})"

class Rational(Pair):
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю!")
        common_divisor = gcd(numerator, denominator)
        super().__init__(numerator // common_divisor, denominator // common_divisor)

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second

    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        num = self.first * other.second + other.first * self.second
        den = self.second * other.second
        return Rational(num, den)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        num = self.first * other.second - other.first * self.second
        den = self.second * other.second
        return Rational(num, den)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.first * other.first, self.second * other.second)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if other.first == 0:
            raise ZeroDivisionError("Деление на ноль!")
        return Rational(self.first * other.second, self.second * other.first)

    def __str__(self):
        if self.second == 1:
            return f"{self.first}"
        return f"{self.first}/{self.second}"

    def __repr__(self):
        return f"Rational({self.first}, {self.second})"


def process_pair(pair1: Pair, pair2: Pair):

    print(f"\nОперации над: {pair1} и {pair2}")
    print(f"Сложение:      {pair1 + pair2}")
    print(f"Вычитание:     {pair1 - pair2}")
    print(f"Умножение:     {pair1 * pair2}")
    try:
        print(f"Деление:       {pair1 / pair2}")
    except ZeroDivisionError as e:
        print(f"Деление:       Ошибка ({e})")


if __name__ == '__main__':

    print("\n[Ввод комплексных чисел]")
    print("Введите первое комплексное число:")
    c1_real = Reader.read_float("  Действительная часть: ")
    c1_imag = Reader.read_float("  Мнимая часть: ")
    c1 = Complex(c1_real, c1_imag)

    print("Введите второе комплексное число:")
    c2_real = Reader.read_float("  Действительная часть: ")
    c2_imag = Reader.read_float("  Мнимая часть: ")
    c2 = Complex(c2_real, c2_imag)

    print("Введите первое рациональное число (числитель и знаменатель):")
    r1_num = Reader.read_int("Числитель: ")
    r1_den = Reader.read_int("Знаменатель: ")
    r1 = Rational(r1_num, r1_den)

    print("Введите второе рациональное число (числитель и знаменатель):")
    r2_num = Reader.read_int("Числитель: ")
    r2_den = Reader.read_int("Знаменатель: ")
    r2 = Rational(r2_num, r2_den)

    print("\nСозданные объекты")
    print(f"Комплексное 1 (str):  {c1}")
    print(f"Комплексное 2 (str):  {c2}")
    print(f"Комплексное 1 (repr): {repr(c1)}")

    print(f"Рациональное 1 (str):  {r1}")
    print(f"Рациональное 2 (str):  {r2}")
    print(f"Рациональное 1 (repr): {repr(r1)}")

    process_pair(c1, c2)
    process_pair(r1, r2)

    print("\nПроверка полиморфизма (список объектов базового класса)")
    pairs = [c1, r1, c2, r2]
    for p in pairs:
        print(f"Объект типа {type(p).__name__}: {p}")