def direction(pole, turn):
    '''
    tells the next direction of the current direction after clock wise or anti-clock wise
    '''

    index_number = 0
    poles = ["E", "S", "W", "N"]
    if (pole in poles) and ("clock wise" in turn or "anti" in turn):
        if "clock wise" in turn:
            index_number = poles.index(pole)
            if index_number >= 3:
                index_number -= 3
            else:
                index_number += 1

        elif "anti" in turn:
            index_number = poles.index(pole)
            index_number -= 1
        return poles[index_number]


if __name__ == "__main__":
    pole = input("enter pole: ").upper()
    turn = input("enter direction: ").lower()
    print(direction(pole, turn))