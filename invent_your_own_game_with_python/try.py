# import random

# while True:
#     usr_toss = input("\n    Toss for whose turn first, your or computer ?\n    heads or tail ? ")
#     toss = random.choice(["heads", "tail"])
#     if usr_toss == toss:
#         print(f"\n    {toss}, You won the toss !")
#     else:
#         print(f"\n    {toss}, Computer won the toss !")

#--------------------------------------------------------------------------------------------------

# import time
# def loading():
#     for i in range(4):
#         for j in ["/", "-", "\\"]:
#             print("loading " + j, end="\r")
#             time.sleep(0.2)


# loading()
# print("\ndone")

#---------------------------------------------------------------------------------------------------

# import os

# width = os.get_terminal_size().columns
# # print("hello".center(width))               

#---------------------------------------------------------------------------------------------------

# board = [" 7 | 8 | 9 ", "---+---+---", "4 | 5 | 6 ", "---+---+---", "1 | 2 | 3 "]
# for i in board:
#     print(type(i))
#     print("hello".center(width))

#--------------------------------------------------------------------------------------------------

# creating 3D data object
# a = []
# for i in range(2):
#     a.append([])
#     for j in range(2):
#         a[i].append([])
#         for k in range(2):
#             a[i][j].append(k)

# print(a)
# print(a[1][1][1])

#-------------------------------------------------------------------------------------------------------
import random

def getNewBoard():
    # Create a new 60x15 board data structure.
    board = []
    for x in range(60): # The main list is a list of 60 lists.
        board.append([])
        for y in range(15): # Each list in the main list has 15 single-character strings.
            # Use different characters for the ocean to make it more readable.
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    tensDigitsLine = '    '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)
    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()
    for row in range(15):
    # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
    boardRow = ''
    for column in range(60):
        boardRow += board[column][row]
    print('%s%s %s %s' % (extraSpace, row, boardRow, row))
    print()
    print('   ' + ('0123456789' * 6))
    print(tensDigitsLine)

drawBoard(getNewBoard())
