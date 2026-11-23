'''
Создать класс Pair (пара чисел);
определить методы изменения полей и вычисления произведения чисел.
Определить производный класс RightAngled с полями-катетами.
Определить методы вычисления гипотенузы и площади треугольника.
Составить программу с использованием иерархии классов.
В раздел программы, начинающийся после инструкции
if __name__ == '__main__':
добавить код, демонстрирующий возможности разработанных классов.
'''
import math


class Pair:

    def __init__(self, first: float = 1.0, second: float = 1.0):
        self.first = first
        self.second = second

    def set_values(self, first: float, second: float):
        self.first = first
        self.second = second
        print(f"Значения пары изменены на: ({self.first}, {self.second})")

    def get_product(self) -> float:
        return self.first * self.second

    def __str__(self):
        return f"Pair({self.first}, {self.second})"


class RightAngled(Pair):

    def __init__(self, a: float = 3.0, b: float = 4.0):
        super().__init__(a, b)

    @property
    def leg_a(self) -> float:
        return self.first

    @leg_a.setter
    def leg_a(self, value: float):
        self.first = value

    @property
    def leg_b(self) -> float:
        return self.second

    @leg_b.setter
    def leg_b(self, value: float):
        self.second = value

    def get_hypotenuse(self) -> float:
        return math.sqrt(self.leg_a ** 2 + self.leg_b ** 2)

    def get_area(self) -> float:
        return 0.5 * self.leg_a * self.leg_b

    def __str__(self):
        return f"RightAngled(катеты: {self.leg_a}, {self.leg_b})"

if __name__ == '__main__':
    pair = Pair(4, 5)
    print(f"Создан объект: {pair}")
    print(f"Произведение чисел: {pair.get_product()}")

    pair.set_values(7, 3)
    print(f"Новое произведение чисел: {pair.get_product()}")

    triangle = RightAngled(3, 4)
    print(f"Создан объект: {triangle}")

    print(f"Произведение катетов: {triangle.get_product()}")

    print(f"Гипотенуза: {triangle.get_hypotenuse():.2f}")
    print(f"Площадь треугольника: {triangle.get_area():.2f}")
    print("\nИзменяем катеты на 6 и 8:")
    triangle.leg_a = 6
    triangle.leg_b = 8

    print(f"Новая гипотенуза: {triangle.get_hypotenuse():.2f}")
    print(f"Новая площадь: {triangle.get_area():.2f}")
    print( isinstance(triangle, Pair))