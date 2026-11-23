import sys
import os
# tests/test_z3.py
import pytest
from oop_4.Zadania.z_3 import Pair, Complex, Rational


def test_abstract_base_class():
    with pytest.raises(TypeError):
        Pair(1, 2)


def test_complex_arithmetic():
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)

    res_add = c1 + c2
    assert res_add.first == 4
    assert res_add.second == 6

    res_mul = c1 * c2
    assert res_mul.first == -5
    assert res_mul.second == 10


def test_complex_division_by_zero():
    c1 = Complex(1, 2)
    c_zero = Complex(0, 0)

    with pytest.raises(ZeroDivisionError):
        c1 / c_zero


def test_rational_arithmetic_and_reduction():
    r1 = Rational(1, 2)
    r2 = Rational(1, 3)

    res_add = r1 + r2
    assert res_add.first == 5
    assert res_add.second == 6

    r3 = Rational(2, 3)
    res_mul = r1 * r3
    assert res_mul.first == 1
    assert res_mul.second == 3


def test_rational_zero_denominator():
    with pytest.raises(ValueError):
        Rational(5, 0)


def test_virtual_call_polymorphism(capsys):
    c = Complex(2, 3)
    r = Rational(1, 2)

    assert isinstance(c, Pair)
    assert isinstance(r, Pair)

    assert str(c) == "(2 + 3i)"
    assert str(r) == "1/2"