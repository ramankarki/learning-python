import random
import time
import os
import re


# sub function ==> loading
def loading(width):
    left_space = (width // 2) - 3
    print()
    for i in range(3):
        for j in ["/", "-", "\\"]:
            print(" " * left_space + "loading " + j, end="\r")
            time.sleep(0.2)


# sub function ==> break_line
def break_line(line, width):
    print()
    print(line * width)
    print()


# sub function ==> board
def board(width):
    board = [f" {tictactoe[7]} | {tictactoe[8]} | {tictactoe[9]} ", "---+---+---", f" {tictactoe[4]} | {tictactoe[5]} | {tictactoe[6]} ", "---+---+---", f" {tictactoe[1]} | {tictactoe[2]} | {tictactoe[3]} "]
    for i in board:
        print(i.center(width))
    print()


# sub function ==> board_reset
def board_reset():
    for i in range(1, 10):
        tictactoe[i] = " "


# sub-sub function ==> ask_play_again
def ask_play_again(width):
    left_space = width // 2 - 11
    print()
    print("Want to play again ?".center(width))
    while True:
        play_again = input(" " * left_space + "# yes or no (y or n): ")
        if play_again == "y" or play_again == "yes":
            print()
            break_line("#", width)
            board_reset()
            main()
        elif play_again == "n" or play_again == "no":
            exit()
        else:
            print("!!! please enter yes or no (y or n).".center(width))
            print()


# sub-sub function ==> won_do_this
def won_do_this(player_name, width):
    print()
    for i in ["############", "## Result ##", "############"]:
        print(i.center(width))
    print("\n")
    board(width)
    print(f"######## {player_name} won the game ########".center(width))
    ask_play_again(width)


# sub function ==> draw_do_this
def draw_do_this(width, draw):
    print()
    for i in ["############", "## Result ##", "############"]:
        print(i.center(width))
    print("\n")
    board(width)
    print(f"######## draw ########".center(width))
    ask_play_again(width)


# sub function ==> check_if_won
def check_if_won(player_name, width, draw):
    if (tictactoe[1] == "X" and tictactoe[2] == "X" and tictactoe[3] == "X") or (tictactoe[1] == "O" and tictactoe[2] == "O" and tictactoe[3] == "O"):
        won_do_this(player_name, width)
    elif (tictactoe[4] == "X" and tictactoe[5] == "X" and tictactoe[6] == "X") or (tictactoe[4] == "O" and tictactoe[5] == "O" and tictactoe[6] == "O"):
        won_do_this(player_name, width)
    elif (tictactoe[7] == "X" and tictactoe[8] == "X" and tictactoe[9] == "X") or (tictactoe[7] == "O" and tictactoe[8] == "O" and tictactoe[9] == "O"):
        won_do_this(player_name, width)
    elif (tictactoe[1] == "X" and tictactoe[4] == "X" and tictactoe[7] == "X") or (tictactoe[1] == "O" and tictactoe[4] == "O" and tictactoe[7] == "O"):
        won_do_this(player_name, width)
    elif (tictactoe[2] == "X" and tictactoe[5] == "X" and tictactoe[8] == "X") or (tictactoe[2] == "O" and tictactoe[5] == "O" and tictactoe[8] == "O"):
        won_do_this(player_name, width)
    elif (tictactoe[3] == "X" and tictactoe[6] == "X" and tictactoe[9] == "X") or (tictactoe[3] == "O" and tictactoe[6] == "O" and tictactoe[9] == "O"):
        won_do_this(player_name, width)
    elif (tictactoe[1] == "X" and tictactoe[5] == "X" and tictactoe[9] == "X") or (tictactoe[1] == "O" and tictactoe[5] == "O" and tictactoe[9] == "O"):
        won_do_this(player_name, width)
    else:
        if (tictactoe[3] == "X" and tictactoe[5] == "X" and tictactoe[7] == "X") or (tictactoe[3] == "O" and tictactoe[5] == "O" and tictactoe[7] == "O"):
            won_do_this(player_name, width)

    for i in range(1, 10):
        if tictactoe[i] == " ":
            break
        else:
            draw += 1
    if draw == 9:
        draw_do_this(width, draw)


# sub function ==> first_player_name
def player_name(player, width, left_space):
    while True:
        first_player = input(" " * left_space + f"# {player} name: ").title()
        if re.search(r"^[a-zA-Z'-]+$", first_player):
            return first_player
        else:
            print("!!! please enter a valid name".center(width))
            print()


def show_info(width):
    left_space = (width // 2) - 8
    print("\n")
    print("Enter the individual number for your moves\n".center(width))
    print("You VS Computer ;-)\n".center(width))

    board_example = [" 7 | 8 | 9 ", "---+---+---", "4 | 5 | 6 ", "---+---+---", "1 | 2 | 3 "]
    for i in board_example:
        print(i.center(width))
    print()
    print("fig: example of tictactoe board.".center(width))


def ask_one_two_player_game(width):
    left_space = (width // 2) - 8
    print()
    print("# choose any one between 1 or 2".center(width))
    print("# option 1 > one player game".center(width))
    print("# option 2 > two player game".center(width))

    while True:
        print()
        vs_player = input(" " * left_space + "# choose any one > ")
        if vs_player == "1":
            while True:
                print()
                name = input(" " * left_space + "# Your name: ").title()
                if re.search(r"^[a-zA-Z'-]+$", name):
                    return ["1", name, "Computer"]
                else:
                    print("!!! please enter a valid name".center(width))

        elif vs_player == "2":
            print()
            first_player = player_name("first player", width, left_space)
            second_player = player_name("second player", width, left_space)
            return ["2", first_player, second_player]
        
        else:
            print("!!! please choose between option (1 or 2)".center(width))
            print()


def ask_symbol(player_name, width):
    left_space = (width // 2) - 8
    print()
    print("Which one you want? 'X' or 'O'".center(width))
    print(("#"+ player_name).center(width))
    print()

    while True:
        symbol = input(" " * left_space + "# choose any one > ")
        if symbol == "X":
            return ["X", "O"]
        elif  symbol == "O":
            return ["O", "X"]
        else:
            print("!!! please choose any one from 'X' or 'O'.\n".center(width))


def toss(width, *player_name):
    left_space = (width // 2) - 8
    print("\n")
    print("Toss".center(width))
    print("------".center(width))
    print("Whose turn first ?".center(width))
    print("head or tail ?".center(width))
    print(("#" + player_name[0]).center(width))

    while True:
        print()
        usr_toss = input(" " * left_space + "# choose any one > ")
        if usr_toss == "head" or usr_toss == "tail":
            break
        else:
            print("!!! please choose any one from head or tail.".center(width))

    toss = random.choice(["head", "tail"])
    if usr_toss == toss:
        loading(width)
        print(f"> {toss}, {player_name[0]} won the toss !".center(width))
        break_line("-", width)
        return ["1", player_name[0], player_name[1]]
    else:
        loading(width)
        print(f"> {toss}, {player_name[1]} won the toss !".center(width))
        break_line("-", width)
        return ["2", player_name[1], player_name[0]]


def usr_turn(player_name, symbol1, width, draw):
    left_space = (width // 2) - 10
    print(f"# {player_name}'s turn: {symbol1}".center(width))
    print()
    board(width)

    while True:
        move = input(" " * left_space + f"# {player_name} move (1-9): ")
        if re.search(r"[1-9]", move) and len(move) == 1:
            print()
        else:
            print("!!! please enter your move from 1-9".center(width))
            print()
            continue

        if  tictactoe[int(move)] != " ":
            print(f"{move} is already used, try another.".center(width))
            print()
            continue

        break

    tictactoe[int(move)] = symbol1
    check_if_won(player_name, width, draw)


# sub function ==> get_board_copy
def get_copy_board():
    copy_board = {}
    for i in range(1, 10):
        copy_board[i] = tictactoe[i]
    return copy_board


# sub function ==> test_win_move
def test_if_won(copy_board, symbol, test_move):
    copy_board[test_move] = symbol
    if (copy_board[1] == symbol and copy_board[2] == symbol and copy_board[3] == symbol):
        return True
    elif (copy_board[4] == symbol and copy_board[5] == symbol and copy_board[6] == symbol):
        return True
    elif (copy_board[7] == symbol and copy_board[8] == symbol and copy_board[9] == symbol):
        return True
    elif (copy_board[1] == symbol and copy_board[4] == symbol and copy_board[7] == symbol):
        return True
    elif (copy_board[2] == symbol and copy_board[5] == symbol and copy_board[8] == symbol):
        return True
    elif (copy_board[3] == symbol and copy_board[6] == symbol and copy_board[9] == symbol):
        return True
    elif (copy_board[1] == symbol and copy_board[5] == symbol and copy_board[9] == symbol):
        return True
    elif (copy_board[3] == symbol and copy_board[5] == symbol and copy_board[7] == symbol):
        return True
    else:
        copy_board[test_move] = " "


# test_fork_moves
def test_fork_moves(copy_board, symbol, test_move):
    # Determines if a move opens up a fork
    copy_board[test_move] = symbol
    winning_moves = 0
    for j in range(1, 10):
        if copy_board[j] == " " and test_if_won(copy_board, symbol, j):
            winning_moves += 1
    copy_board[test_move] = " "
    return winning_moves >= 2


#sub function ==> get_pc_move
def get_pc_move(copy_board, symbol1, symbol2):
    # check if pc wins
    for i in range(1, 10):
        if copy_board[i] == " " and test_if_won(copy_board, symbol2, i):
            return i
    
    # check if usr wins
    for i in range(1, 10):
        if copy_board[i] == " " and test_if_won(copy_board, symbol1, i):
            return i

    # Check computer fork opportunities
    for i in range(1, 10):
        if copy_board[i] == " " and test_fork_moves(copy_board, symbol2, i):
            return i

    # check usr fork opportunities
    player_forks = 0
    for i in range(1, 10):
        if copy_board[i] == " " and test_fork_moves(copy_board, symbol1, i):
            player_forks += 1
            temp_move = i
    if player_forks == 1:
        return temp_move
    elif player_forks == 2:
        for j in [2, 4, 6, 8]:
            if copy_board[j] == " ":
                return j

    # play corners
    for i in [1, 3, 7, 9]:
        if copy_board[i] == " ":
            return i

    # play center
    if copy_board[5] == " ":
        return 5

    # play sides
    for i in [2, 6, 4, 8]:
        if copy_board[i] == " ":
            return i


def computer_turn(player_name, width, symbol1, symbol2, draw):
    copy_board = get_copy_board()
    move = get_pc_move(copy_board, symbol1, symbol2)
    tictactoe[int(move)] = symbol2
    check_if_won(player_name, width, draw)
    print(f"# {player_name}'s turn: {symbol2}".center(width))
    time.sleep(0.4)
    print()
    board(width)
    print(f"# Computer move: {move}\n".center(width))


def main():
    draw = 0

    # getting terminal width size
    width = os.get_terminal_size().columns

    # showing basic info. of game
    show_info(width)
    time.sleep(1)

    # ask for one or two payer game
    vs_game, first_player, second_player = ask_one_two_player_game(width)

    # asking for their symbol
    symbol1, symbol2 = ask_symbol(first_player, width)

    # whose turn first ?
    num, first_turn, second_turn = toss(width, first_player, second_player)

    # sleep for 1 sec
    time.sleep(1)

    # starting game
    start_game = ["####################", "## start the game ##", "####################"]
    for i in start_game:
        print(i.center(width))
    print()

    # sleep for 1 sec
    time.sleep(1)

    # game play
    while True:
        # one player game
        if vs_game == "1":
            if first_turn == "Computer":
                while True:
                    computer_turn(first_turn, width, symbol1, symbol2, draw)
                    usr_turn(second_turn, symbol1, width, draw)
            else:
                while True:
                    usr_turn(first_turn, symbol1, width, draw)
                    computer_turn(second_turn, width, symbol1, symbol2, draw)

        # two player game
        else:
            if num == "1":
                while True:
                    usr_turn(first_turn, symbol1, width, draw)
                    usr_turn(second_turn, symbol2, width, draw)
            else:
                while True:
                    usr_turn(first_turn, symbol2, width, draw)
                    usr_turn(second_turn, symbol1, width, draw)


tictactoe = {
    1 : " ",
    2 : " ",
    3 : " ",
    4 : " ",
    5 : " ",
    6 : " ",
    7 : " ",
    8 : " ",
    9 : " "
}


if __name__ == "__main__":
    main()

