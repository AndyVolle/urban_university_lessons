import random

from termcolor import cprint

# Константы
MIN_FULLNESS = 20
MAX_FULLNESS = 100
FOOD_COST = 50
WORK_INCOME = 50
INIT_FOOD = 10
INIT_MONEY = 50
DAYS = 365

class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = MAX_FULLNESS // 2
        self.house = None

    def __str__(self):
        return f'я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='yellow', force_color=True)
            self.fullness = min(self.fullness + 10, MAX_FULLNESS)
            self.house.food -= 10
        else:
            cprint(f'{self.name} нет еды', color='light_red', force_color=True)

    def shopping(self):
        if self.house.money >= FOOD_COST:
            cprint(f'{self.name} сходил в магаззин за едой', color='magenta', force_color=True)
            self.house.money -= FOOD_COST
            self.house.food += FOOD_COST
        else:
            cprint(f'{self.name} деньги закончились', color='red', force_color=True)

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue', force_color=True)
        self.house.money += WORK_INCOME
        self.fullness = max(self.fullness - 10, 0)

    def watch_MTV(self):
        cprint(f'{self.name} смотрел MTV целый день', color='green', force_color=True)
        self.fullness = max(self.fullness - 10, 0)

    def go_into_house(self, house):
        self.house = house
        cprint(f'{self.name} въехал в дом!!!', color='cyan', force_color=True)

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер...', color='light_red', force_color=True)
            return
        if self.fullness < MIN_FULLNESS:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < FOOD_COST:
            self.work()
        else:
            random.choice([self.work, self.eat, self.watch_MTV])()


class House:
    def __init__(self):
        self.food = INIT_FOOD
        self.money = INIT_MONEY

    def __str__(self):
        return f'в доме осталось еды {self.food}, денег {self.money}'


citizens = [Man(name) for name in ('Бивис', 'Батхед', 'Кенни')]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_house(house=my_sweet_home)

for day in range(1, DAYS + 1):
    cprint(f'==================== День {day} ====================')
    for citizen in citizens:
        citizen.act()
    print('--------------------в конце дня-----------------------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)
