import random

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return f'я - {self.name}, сытость {self.fullness}'

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} поел', color='yellow', force_color=True)
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint(f'{self.name} нет еды', color='light_red', force_color=True)

    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} сходил в магаззин за едой', color='magenta', force_color=True)
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'{self.name} деньги закончились', color='red', force_color=True)

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue', force_color=True)
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint(f'{self.name} смотрел MTV целый день', color='green', force_color=True)
        self.fullness -= 10

    def go_into_house(self, house):
        self.house = house
        cprint(f'{self.name} въехал в дом!!!', color='cyan', force_color=True)

    def act(self):
        if self.fullness < 0:
            cprint(f'{self.name} умер...', color='light_red', force_color=True)
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()
        # elif dice == 3:
        #     self.eat()
        # elif dice == 4:
        #     self.eat()
        # elif dice == 5:
        #     self.eat()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return f'в доме осталось еды {self.food}, денег {self.money}'


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_house(house=my_sweet_home)

for day in range(1, 366):
    cprint(f'==================== День {day} ====================')
    for citizen in citizens:
        citizen.act()
    print('--------------------в конце дня-----------------------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)

# print(vasya)
# vasya.eat()
# print(vasya)
# vasya.work()
# print(vasya)
# vasya.play_DOTA()
# print(vasya)
