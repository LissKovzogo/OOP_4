import sys
import os

# tests/test_z2.py
import pytest
from oop_4.Zadania.z_2 import Pair, RightAngled


def test_pair_init_and_product():
    p = Pair(4, 5)
    assert p.get_product() == 20


def test_pair_set_values():
    p = Pair(1, 1)
    p.set_values(7, 3)
    assert p.first == 7
    assert p.second == 3
    assert p.get_product() == 21


def test_rightangled_inheritance():
    t = RightAngled(3, 4)

    assert isinstance(t, Pair)

    assert t.get_area() == 6.0

    assert t.get_hypotenuse() == 5.0


def test_rightangled_properties(capsys):
    t = RightAngled(1, 1)

    t.leg_a = 6
    t.leg_b = 8

    assert t.first == 6
    assert t.second == 8
    assert t.get_hypotenuse() == 10.0


def test_str_methods():
    p = Pair(2.5, 4.0)
    t = RightAngled(3, 4)

    assert str(p) == "Pair(2.5, 4.0)"
    assert str(t) == "RightAngled(катеты: 3, 4)"
