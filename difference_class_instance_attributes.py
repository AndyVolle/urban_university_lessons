import random

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return f'я - {self.name}, сытость {self.fullness}, еды осталось {self.food}, денег осталось {self.money}'

    def eat(self):
        if self.food >= 10:
            cprint(f'{self.name} поел', color='yellow', force_color=True)
            self.fullness += 10
            self.food -= 10
        else:
            cprint(f'{self.name} нет еды', color='light_red', force_color=True)

    def shopping(self):
        if self.money >= 50:
            cprint(f'{self.name} сходил в магаззин за едой', color='magenta', force_color=True)
            self.money -= 50
            self.food += 50
        else:
            cprint(f'{self.name} деньги закончились', color='red', force_color=True)

    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue', force_color=True)
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        cprint(f'{self.name} играл в доту целый день', color='green', force_color=True)
        self.fullness -= 10

    def act(self):
        if self.fullness < 0:
            cprint(f'{self.name} умер...', color='light_red', force_color=True)
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()
        # elif dice == 3:
        #     self.eat()
        # elif dice == 4:
        #     self.eat()
        # elif dice == 5:
        #     self.eat()


vasya = Man(name='Вася')
for day in range(1, 21):
    cprint(f'==================== День {day} ====================')
    vasya.act()
    print(vasya)

# print(vasya)
# vasya.eat()
# print(vasya)
# vasya.work()
# print(vasya)
# vasya.play_DOTA()
# print(vasya)
