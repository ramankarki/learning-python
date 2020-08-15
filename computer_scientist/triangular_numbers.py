def triangular_numbers(n):
    '''
    print the triangular numbers.
    '''
    sum = 0
    for i in range(1, n+1):
        sum += i
        print(f"{i}\t{sum}")


triangular_numbers(10)