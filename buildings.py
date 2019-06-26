import random
import sys
import os
import mainprogram

"""
Ranch

"""
worker_ranch = False


class Rancher:
    def __init__(self, name):
        self.name = name


class Ranch:
    cows = 0

    chickens = 0

    cows_product = 0

    chickens_product = 0

    units_food_s = 0

    cows_season = 0

    chickens_season = 0

    @staticmethod
    def manage_ranch():
        c = random.randint(1, 3)
        Ranch.cows_season = c

        c2 = random.randint(1, 5)
        Ranch.chickens_season = c2

        Ranch.cows += c
        Ranch.chickens += c2

        Ranch.cows_product = Ranch.cows
        Ranch.chickens_product = Ranch.chickens

        Ranch.units_food_s = Ranch.cows_product + Ranch.chickens_product

    @staticmethod
    def menu():
        global worker_ranch

        os.system("cls")

        print("~" * 50)
        print('RANCH')
        print("~" * 50)
        while not worker_ranch:

            print('hire a rancher')
            print('-' * 42)
            mainprogram.list_chars()
            print('\na) view characters')
            print('c) to choose worker')
            pi = input('>> ')
            if pi == str('a'):
                mainprogram.view_char()
                Ranch.menu()
            elif pi == str('c'):
                indexx = int(input('input character number > ')) - 1
                print('\n')
                print(str(mainprogram.result[indexx]["name"]))
                print('\n')
                print('press "h" to hire selected')
                print('press "b" to go back')
                pi = input('> ')
                if pi == 'h':
                    worker_ranch = True
                    Rancher.name = str(mainprogram.result[indexx]["name"])
                    mainprogram.result[indexx]["job"] = str('rancher')
                    new = open("character" + " " + str(mainprogram.result[indexx]["name"]), "w")
                    new.write("character name" + " " + mainprogram.result[indexx]["name"])
                    new.write("\n" + "character age" + " " + str(mainprogram.result[indexx]["age"]))
                    new.write("\n" + "character job" + " " + str('rancher'))
                    new.write("\n" + "life expectancy" + " " + str(mainprogram.result[indexx]["life_exp"]))
                    new.close()

                    print('rancher is now {}'.format(Rancher.name))
                    input('ok...')
                    # Ranch.menu()
                elif pi == 'b':
                    Ranch.menu()

        else:
            os.system("cls")
            print("~" * 50)
            print('RANCH')
            print("~" * 50)

            if mainprogram.search_dictionaries('name', Rancher.name, mainprogram.result):
                # if list(filter(lambda dic: dic['name'] == Rancher.name, result)):

                print('rancher: {}'.format(Rancher.name))
                print('\n')
                print('number of total cows: {}'.format(Ranch.cows))
                print('number of total chickens: {}'.format(Ranch.chickens))
                print('number of cows this season: {}'.format(Ranch.cows_season))
                print('number of chickens this season: {}'.format(Ranch.chickens_season))
                print('total food: {}'.format(mainprogram.total_food))
                print('total food expected this season: {}'.format(mainprogram.total_food + Ranch.units_food_s))
                print("-----")
                input('>... ')
            else:
                print('ranger is dead')
                print("-----")
                input('>... ')
                worker_ranch = False
                Rancher.name = None
