'''
В некоторой игре-стратегии есть солдаты и герои.
У всех есть свойство, содержащее уникальный номер объекта, и свойство,
в котором хранится принадлежность команде. У солдат есть метод "иду за героем",
который в качестве аргумента принимает объект типа "герой".
У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды.
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним.
Выведите на экран идентификационные номера этих двух юнитов.
'''
import random


class Unit:
    _id_counter = 1

    def __init__(self, team: str):
        self.id = Unit._id_counter
        Unit._id_counter += 1
        self.team = team

    def __str__(self):
        return f"{self.__class__.__name__} (ID: {self.id}, Команда: {self.team})"


class Hero(Unit):

    def __init__(self, team: str):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Герой команды {self.team} повысил уровень до {self.level}!")


class Soldier(Unit):

    def __init__(self, team: str):
        super().__init__(team)

    def follow_hero(self, hero: Hero):
        print(
            f"Солдат (ID: {self.id}) из команды '{self.team}' теперь следует за Героем (ID: {hero.id}) из команды '{hero.team}'.")

if __name__ == "__main__":
    print("Создание героев")
    hero_red = Hero(team="Красные")
    hero_blue = Hero(team="Синие")
    print(f"Создан: {hero_red}")
    print(f"Создан: {hero_blue}")

    print("\nГенерация солдат")
    red_soldiers = []
    blue_soldiers = []

    for _ in range(20):
        team = random.choice(["Красные", "Синие"])
        soldier = Soldier(team=team)

        if team == "Красные":
            red_soldiers.append(soldier)
        else:
            blue_soldiers.append(soldier)

    print(f"Сгенерировано солдат: Красные - {len(red_soldiers)}, Синие - {len(blue_soldiers)}")

    print("\nСравнение сил и повышение уровня")
    print(f"Длина списка 'Красных': {len(red_soldiers)}")
    print(f"Длина списка 'Синих': {len(blue_soldiers)}")

    if len(red_soldiers) > len(blue_soldiers):
        hero_red.level_up()
    elif len(blue_soldiers) > len(red_soldiers):
        hero_blue.level_up()
    else:
        print("Ничья! У обеих команд одинаковое количество солдат. Уровни не изменились.")

    print("\nОтправка солдата за героем")

    if red_soldiers:
        first_soldier_of_hero_red = red_soldiers[0]
        first_soldier_of_hero_red.follow_hero(hero_red)

        print("\nИдентификационные номера")
        print(f"ID Героя (первого): {hero_red.id}")
        print(f"ID Солдата (первого героя): {first_soldier_of_hero_red.id}")
    else:
        print("У первого героя (Красные) нет солдат, чтобы отправить кого-то за ним.")