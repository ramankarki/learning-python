def collatz(n):
    '''
    Print the 3n+1 sequence from n,
    terminating when it reaches 1.
    '''

    print("sequence: ", end="")
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    print(n, end=". \n")


collatz(3)
            