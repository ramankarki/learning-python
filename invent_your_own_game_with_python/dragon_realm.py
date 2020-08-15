import random
import time


def info():
    print('''
    You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.\n
    ''')


def choose_cave():
    cave = ""
    while cave != "1" or cave != "2":
        cave = input("    which cave you will go in to?\n    (1 or 2): ")
        if cave == "1" or cave == "2":
            return cave
        elif cave == "exit":
            exit()
        else:
            print("    please enter a valid cave number...\n")


def check_cave(cave_number):
    number = random.randint(1, 2)

    print("\n    You approach the cave...\n")
    time.sleep(2)
    print("    It is dark and spooky...\n")
    time.sleep(2)
    print("    A large dragon jumps out in front of you! He opens his jaws and...\n")
    time.sleep(2)

    if str(number) == cave_number:
        print("    Gives you his treasure!")
    else:
        print("    Gobbles you down in one bite!")


while True:
    info()
    time.sleep(2)
    cave_number = choose_cave()
    time.sleep(2)
    check_cave(cave_number)
    time.sleep(2)
    
    while True:
        play_again = input("\n    Do you want to play again?\n    yes or no (y or n): ")
        if play_again == "y" or play_again == "yes":
            break
        elif play_again == "n" or play_again == "no":
            exit()
        else:
            continue
