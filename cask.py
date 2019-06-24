import itertools

import buildingss
import mainnew

ci = 0
number_chars_died = 0

p1 = itertools.product(mainnew.one_name, mainnew.one_name2)
pk = list(p1)
p2 = itertools.product(mainnew.one_job)
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
        foods += buildingss.Ranch.units_food_s
        return foods
