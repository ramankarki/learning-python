bd = [
    [0,0,0,1,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0]
]


def share_diagonal(x0,y0,x1,y1):
    '''
    returns true if diagonals clashes
    '''
    x = abs(x1-x0)
    y = abs(y1-y0)
    return x == y   # if they are in same diagonal, x is always equal to y


def col_clashes(board, c):
    '''
    returns true if column c,
    clashes with any of the column to the left
    '''
    for i in range(c):
        if share_diagonal(i,board[i],c,board[c]):   # right side cordinate will be the same
            return True                             # and will compare with every left side cordinate
    return False


def has_clashes(board):
    '''
    checks whether any of the queen clashes with any other queen diagonally,
    we assume the numbers to be the permutation of the column numbers
    '''
    for i in range(1, len(board)):
        if col_clashes(board,i):    # deliver every column value except first column
            return True
    return False


def main(size):
    import random
    numbers = list(range(size))
    counter = 0                 # searching for 10 different solutions
    tries = 1                   # counter for how many tries occured
    solutions = []
    while counter < 10:
        random.shuffle(numbers)         # shuffle each time 
        if not has_clashes(numbers):                             # if it doesn't have any clashes,
            if tuple(numbers) not in solutions:
                solutions.append(tuple(numbers))
                if __name__ == "__main__":
                    print(f"Found solution {numbers} in {tries} tries.") # we found solution
                counter += 1                                         # and increase the counter value.
            tries = 1                                            # reset the tries value for next solution
        tries += 1                                               # increment tries value if not found
    return solutions


if __name__ == "__main__":
    main(8)

