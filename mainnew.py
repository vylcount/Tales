import os
import random
import os.path
import sys
import program1
import buildings
import textwrap
import cProfile
import colorama
import dill
import math
import itertools
import numpy
import time
import profile
import re
import multiprocessing as mp
import cProfile, pstats, io
from pstats import SortKey

# from colorama import Back, Fore, Style, init
#
# init(autoreset=True)
# print(Fore.RED + 'some red text')

characters = 0
result = []
nameslist = set()
nameslist2 = []
namesload = []
total_food = 0

# def profileit(func):
#     def wrapper(*args, **kwargs):
#         datafn = func.__name__ + ".profile"  # Name the data file sensibly
#         prof = cProfile.Profile()
#         retval = prof.runcall(func, *args, **kwargs)
#         prof.dump_stats(datafn)
#         return retval
#
#     return wrapper


with open("C:\\Users\\User\\Desktop\\first names.txt") as names_file:
    one_name = names_file.read().splitlines()
with open("C:\\Users\\User\\Desktop\\second names.txt") as names_file2:
    one_name2 = names_file2.read().splitlines()
with open("C:\\Users\\User\\Desktop\\jobs.txt") as jobs_file:
    one_job = jobs_file.read().splitlines()


def generate_name():
    first_name = random.choice(one_name)
    second_name = random.choice(one_name2)
    choose_name = (first_name + " " + second_name).title()

    while choose_name not in nameslist:
        nameslist.add(choose_name)
        nameslist2.append(choose_name)


def generate_job():
    choose_job = random.choice(one_job).title()

    return choose_job


def add_character():
    global characters
    characters += 1

    name_go = nameslist2[0]
    name_g = name_go
    # namesload.append(name_g)
    nameslist2.pop(0)

    job_g = generate_job()
    age_g = 102
    # int(random.randint(12, 102))
    life_exp_g = (int(math.ceil(((105 - age_g) / 3 * 2) + random.randint(0, 8))))

    cha = {"name": name_g, "job": job_g, "age": age_g, "life_exp": life_exp_g}
    result.append(cha)


def create_txt_char():
    for x in result:
        if os.path.exists("character" + " " + x['name']):
            continue
        with open("character" + " " + x['name'], "w+") as new:
            new.write("character name" + " " + x['name'])
            new.write("\n" + "character age" + " " + str(x['age']))
            new.write("\n" + "character job" + " " + str(x['job']))
            new.write("\n" + "life expectancy" + " " + str(x['life_exp']))


def addcha(n):
    for aa in range(n):
        add_character()


def show_num_chars_ingame():
    global characters

    print("characters currently in the game: {}".format(characters))


def list_chars():
    for i, pp in enumerate(result, start=1):
        print("{}: {}".format(i, pp))


def change_name_char(selection):
    os.system("cls")
    print("~" * 50)
    print("~" * 50)

    list_chars()
    print("-" * 29)
    print("change which character name?")
    indexx = int(input('> ')) - 1
    x = (result[indexx]).copy()

    print("change" + " " + "{}".format(result[indexx]["name"]))
    x["name"] = str(input("to \n> {}".format(selection)))  # if you want to change name
    os.system("cls")
    print("~" * 50)
    print("~" * 50)

    print(
        "changed name to {}".format(x["name"]), "from {}".format(result[indexx]["name"])
    )
    os.rename(
        "character" + " " + str(result[indexx]["name"]),
        "character" + " " + str(x["name"]),
    )
    result[indexx] = x.copy()

    new = open("character" + " " + str(result[indexx]["name"]), "w")
    new.write("character name" + " " + result[indexx]["name"])
    new.write("\n" + "character age" + " " + str(result[indexx]["age"]))
    new.write("\n" + "character job" + " " + str(result[indexx]["job"]))
    new.write("\n" + "life expectancy" + " " + str(result[indexx]["life_exp"]))
    new.close()
    input('\nok...')


def remove_char():
    os.system("cls")
    print("~" * 50)
    print("~" * 50)

    list_chars()
    print("-" * 29)
    global characters

    print("remove which character?")
    indexx = int(input('> ')) - 1
    os.system("cls")
    print("~" * 50)
    print("~" * 50)
    print(result[indexx])
    print("removed character {}".format(result[indexx]["name"]))
    print("-" * 29)
    os.remove("character" + " " + str(result[indexx]["name"]))
    result.pop(indexx)  # if you want to remove character
    characters -= 1

    list_chars()


def view_char():
    """
    Currently changes the values of characters in the text
    file upon entering the said text file only

    """
    os.system("cls")
    print("~" * 50)
    print("~" * 50)

    show_num_chars_ingame()
    print("\n")
    list_chars()
    print("-" * 42)
    print("view which character?")
    indexx = int(input('> ')) - 1
    try:

        new = open("character" + " " + str(result[indexx]["name"]), "w+")
        new.write("character name" + " " + result[indexx]["name"])
        new.write("\n" + "character age" + " " + str(result[indexx]["age"]))
        new.write("\n" + "character job" + " " + str(result[indexx]["job"]))
        new.write("\n" + "life expectancy" + " " + str(result[indexx]["life_exp"]))
        new.close()
        with open("character" + " " + str(result[indexx]["name"]), 'r') as r:
            os.system("cls")
            print("~" * 50)
            print("~" * 50)
            print(r.read())
            print("\n" + str(result[indexx]))
            input('ok')
    except IndexError:
        print('Character number you entered is not available')


def debug():
    global characters
    change_name_char("")
    remove_char()


def death_char():
    """
Remove characters

    """
    for x in result:
        if x['life_exp'] > -1:
            continue
            # os.remove("character" + " " + str(x["name"]))
        program1.characters_died()
        result.remove(x)
        # [result.remove(x) for x in result if x['life_exp'] > -1]
        program1.character_count(0, 1)


def remove_char_file():
    """
Remove characters txt files

    """
    for x in result:
        if x['life_exp'] > -1:
            continue
        os.remove("character" + " " + str(x["name"]))


# os.system("cls")
# print("~" * 50)
# print("~" * 50)
#
# list_chars()
# print("-" * 29)


def aging():
    for x in result:
        x['age'] += 1
        x['life_exp'] -= 1
        continue


def pri_mortgage():
    for x in result:
        if x['life_exp'] > 0:
            continue
        print("character {}, age: {}, life expectancy: {}".format(x["name"], x['age'], x['life_exp']))


class Turns:
    game_year = 1740
    seasons = 0

    @staticmethod
    def game_year_increment():
        Turns.seasons += 1
        if Turns.seasons == 12:
            Turns.seasons = 1
            Turns.game_year += 1


def end_of_turn_events():
    global total_food
    Turns.game_year_increment()
    os.system("cls")
    print("~" * 50)
    print('End of Turn Events')
    print("~" * 50)
    print('year: {}'.format(Turns.game_year))
    print('season: {}'.format(Turns.seasons))
    print('*' * 29)

    print('Units of food gained this season: {}'.format(buildings.Ranch.units_food_s))
    # except NameError:
    #     print('there is no rancher in the ranch')
    total_food += program1.Kingdomfood.total(0)
    print('total food: {}'.format(math.floor(total_food)))
    total_food -= (program1.ci / 2)
    if total_food <= 0:
        total_food = 0

    print('Units of food consumed this season: {}'.format((program1.ci / 2)))
    print('total food after: {}'.format(math.floor(total_food)))
    print('*' * 29)

    """
    age every character by 1
    kill any characters with life expectancy below 0

    """
    aging()
    remove_char_file()
    for _ in itertools.repeat(None, 6):
        death_char()
    pri_mortgage()

    print("-----")
    input('>... ')


def search_dictionaries(key, value, list_of_dictionaries):
    return [element for element in list_of_dictionaries if element[key] == value]


p1 = itertools.product(one_name, one_name2)
pk = list(p1)
p2 = itertools.product(one_job)
pk2 = list(p2)


def debugg():
    print("-" * 29)
    print('[DEBUG]\n')
    print('names generated: ' + str(len(nameslist)))
    print('names used: ' + str(len(nameslist2)))
    program1.show_char_count()
    print('possible names: {}'.format(len(pk)))
    print('possible jobs: {}'.format(len(pk2)))
    print(">" * 29 + '\n')
