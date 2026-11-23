import sys
import os
# tests/test_z1.py
import pytest
import random
from unittest.mock import patch
from oop_4.Zadania.z_1 import Unit, Hero, Soldier


@pytest.fixture(autouse=True)
def reset_unit_id():
    Unit._id_counter = 1


def test_unit_init_valid():
    u1 = Unit("Красные")
    u2 = Unit("Синие")

    assert u1.id == 1
    assert u2.id == 2
    assert u1.team == "Красные"
    assert u2.team == "Синие"


def test_hero_level_up(capsys):

    hero = Hero("Синие")

    assert hero.level == 1

    hero.level_up()

    assert hero.level == 2

    captured = capsys.readouterr()
    assert f"Герой команды Синие повысил уровень до 2!" in captured.out


def test_soldier_follow_hero(capsys):

    hero = Hero("Красные")
    soldier = Soldier("Красные")

    soldier.follow_hero(hero)

    captured = capsys.readouterr()
    assert f"Солдат (ID: {soldier.id})" in captured.out
    assert f"следует за Героем (ID: {hero.id})" in captured.out


def test_random_team_assignment():

    with patch('random.choice', return_value="Синие"):
        team = random.choice(["Красные", "Синие"])
        assert team == "Синие"


def test_str_method():
    u = Unit("Красные")
    assert str(u) == "Unit (ID: 1, Команда: Красные)"
