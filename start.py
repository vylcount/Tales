import sys
import numpy
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

import program1
import mainprogram
import buildings
# from buildings import Ranch

""" Program Initialization """

filename = "globalsave.pkl"
game_running = True


while len(mainprogram.nameslist) < 1824:
    mainprogram.generate_name()


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
    mainprogram.debugg()

    player_input = input(">>")

    if player_input == "1":
        os.system("cls")
        print("~" * 50)
        print("~" * 50)
        print("How many characters you want to add? ")

        mainprogram.debugg()
        pi = input('> ')

        mainprogram.addcha(int(pi))
        program1.character_count(pi, 0)
        mainprogram.create_txt_char()

        # mainprogram.debug()
        program1.Kingdom.menu()
        mainprogram.end_of_turn_events()
        print("-----")
        input(">> Go to menu ")

    elif player_input == "2":
        os.system("cls")
        print("~" * 50)
        print("~" * 50)

        dill.dump_session(filename)
        print("game saved!")
        input('\nok...')
        mainprogram.debugg()
    elif player_input == "3":
        os.system("cls")
        print("~" * 50)
        print("~" * 50)

        game_running = False
        dill.load_session(filename)
        print("game loaded!")
        print(mainprogram.namesload)
        input('\nok...')
        mainprogram.debugg()
    elif player_input == "4":
        if program1.ci == 0:
            print('There are no characters')
            input('\nok...')
        else:
            mainprogram.view_char()
            mainprogram.debugg()
            input('\nok...')
    elif player_input == "5":
        print('\ncharacters died: {}'.format(program1.number_chars_died))
        input('\nok...')

print("\n-----------------")
print(sys.version)
