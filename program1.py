import itertools

import buildings
import mainprogram

ci = 0
number_chars_died = 0

p1 = itertools.product(mainprogram.one_name, mainprogram.one_name2)
pk = list(p1)
p2 = itertools.product(mainprogram.one_job)
pk2 = list(p2)


def characters_died():
    global number_chars_died
    number_chars_died += 1
    return number_chars_died


def character_count(addcount, subcount):
    global ci
    ci += int(addcount)
    ci -= int(subcount)


def show_char_count():
    global ci
    print(ci)


"""
food to be consumed
"""


class Kingdomfood:
    @staticmethod
    def total(foods=0):
        foods += buildings.Ranch.units_food_s
        return foods


building = ['ranch', 'graveyard']


def list_buildings():
    for i, pp in enumerate(building, start=1):
        print("{}: {}".format(i, pp))


class Kingdom:
    @staticmethod
    def menu():
        print('press (1) kingdom buildings')
        print('press (2) to go back to kingdom menu')
        player_input = input(">>")

        if player_input == "1":
            print("~" * 50)
            print('kingdom buildings')
            print("~" * 50)
            list_buildings()
            print("enter which building?")
            indexx = int(input('> ')) - 1

            if building[indexx] == 'ranch':
                buildings.Ranch.manage_ranch()
                buildings.Ranch.menu()
