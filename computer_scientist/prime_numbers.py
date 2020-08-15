def prime(n):
    n = int(n)
    list_pre = [2, 3, 5, 7, 11]
    if n in list_pre:
        return f"{str(n)} is a prime number."
    elif n == 1:
        return f"{n} is not a prime number."
    else:
        for i in list_pre:
            if n % i == 0:
                return f"{str(n)} is not a prime number."
    return f"{str(n)} is a prime number."


if __name__ == "__main__":
    count = 0
    initial = 1000
    final = 2001
    for i in range(initial, final):
        result = prime(i)
        if "is a prime number." in result:
            print(result)
            count += 1

    print(f"Total prime numbers between {initial}-{final}:", count)
