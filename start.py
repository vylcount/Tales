import sys
import numpy

import cask
import mainnew
import buildings
# from buildings import Ranch
import dill
import pickle
import math
import os
import shelve
import multiprocessing as mp
from multiprocessing import Pool
import cProfile
import profile
import re
import cProfile, pstats, io
from pstats import SortKey

""" Program Initialization """

filename = "globalsave.pkl"
game_running = True

# pr = cProfile.Profile()
# pr.enable()
while len(mainnew.nameslist) < 1824:
    mainnew.generate_name()
# ss2 = sorted(nameslist2)
# print(ss2)

# print('\n')
# ss = sorted(nameslist)
# print(ss)
# pr.disable()
# s = io.StringIO()
# sortby = SortKey.CUMULATIVE
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())


""" Game Initialization """

while game_running:
    os.system("cls")
    print("~" * 50)
    print("~" * 50)

    print("press (1) to start game")
    print("press (2) to save game")
    print("press (3) to load game")
    print("press (4) to view characters")
    print("press (5) to view stats")
    mainnew.debugg()

    player_input = input(">>")

    if player_input == "1":
        os.system("cls")
        print("~" * 50)
        print("~" * 50)
        print("How many characters you want to add? ")

        mainnew.debugg()
        pi = input('> ')
        # pr = cProfile.Profile()
        # pr.enable()
        mainnew.addcha(int(pi))
        cask.character_count(pi, 0)

        # pr.disable()
        # s = io.StringIO()
        # sortby = SortKey.CUMULATIVE
        # ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        # ps.print_stats()
        # print(s.getvalue())

        # debug()
        mainnew.create_txt_char()
        buildings.Ranch.manage_ranch()
        buildings.Ranch.menu()
        mainnew.end_of_turn_events()
        print("-----")
        input(">> Go to menu ")

    elif player_input == "2":
        os.system("cls")
        print("~" * 50)
        print("~" * 50)

        dill.dump_session(filename)
        # pickleout = open("dict.pickle", "wb")
        # pickle.dump([namesload, chas], pickleout)
        # pickleout.close()
        print("game saved!")
        input('\nok...')
        mainnew.debugg()
    elif player_input == "3":
        os.system("cls")
        print("~" * 50)
        print("~" * 50)

        game_running = False
        dill.load_session(filename)
        # picklein = open("dict.pickle", "rb")
        # exm = pickle.load(picklein)
        print("game loaded!")
        print(mainnew.namesload)
        input('\nok...')
        mainnew.debugg()
    elif player_input == "4":
        if cask.ci == 0:
            print('There are no characters')
            input('\nok...')
        else:
            mainnew.view_char()
            mainnew.debugg()
            input('\nok...')
    elif player_input == "5":
        print('\ncharacters died: {}'.format(cask.number_chars_died))
        input('\nok...')

print("\n-----------------")
print(sys.version)
