import random
import re


def enter_name():
    for i in range(3):
        print("Your name: ", end="")
        player_name = input().title()
        if player_name:
            if re.search(r"^[a-zA-Z'-]+$", player_name):
                return player_name
            if i != 2:
                print("# Enter a valid name...\n")
        else:
            print("# Please enter your name...\n")
            continue
    print("Program stopped !")
    exit()


def random_number(player_name):
    number = random.randint(0, 10)
    print(f"Hey! {player_name}, tell me the number I have guessed from 1-10.\n")
    return number


def user_input_check(player_name, number):
    count = 5
    for i in range(5):
        count -= 1
        try:
            input_number = int(input("> "))
        except:
            print("# Please enter a number...\n")
            continue

        if (input_number < 0 or input_number > 10) and (i != 2):
            print("# Please enter a number between 0-10.\n")
            continue

        if number == input_number:
            print(f"You guessed it right {player_name}. It was {input_number}.")
            exit()
        else:
            if number > input_number and (i != 4):
                print(f"# You guessed it low {player_name}\n")
            if number < input_number and (i != 4):
                print(f"# You guessed it high {player_name}\n")

        if number != input_number and (count <= 3):
            if count != 0:
                print(f"# Try last {count} times.")


def main():
    player_name = enter_name()
    number = random_number(player_name)
    user_input_check(player_name, number)
    print(f"\nIn off trying {player_name}, It was {number}")


if __name__ == "__main__":
    main()
