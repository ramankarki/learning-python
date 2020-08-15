def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


print(fib(7))

