import random
from search import timsort


def ticket_gen():
    n_list = []
    for i in range(2):
        n_list.append(random_num(6,1,49))
    return n_list


def lotto_match(array1=None, array2=None):
    if array1 == None and array2 == None:
        array1 = ticket_gen()[0]
        array2 = ticket_gen()[1]

    array1 = timsort(array1)
    array2 = timsort(array2)
    f = 0
    s = 0
    counter = 0
    while True:
        if f >= len(array1):
            return counter
        if s >= len(array2):
            return counter

        if array1[f] == array2[s]:
            counter += 1
            f += 1
            s += 1
        elif array1[f] < array2[s]:
            f += 1
        else:
            s += 1


def is_prime(n):
    least_prime = [2,3,5,7,11]
    for i in least_prime:
        if n == 1:
            return False
        elif n % i == 0:
            return False
    return True


def prime_in(array):
    least_prime = [2,3,5,7,11]
    prime_collect = []
    remaining = []
    for i in array:
        if i in least_prime:
            prime_collect.append(i)
        else:
            remaining.append(i)

    for i in remaining:
        if is_prime(i):
            prime_collect.append(i)

    return len(prime_collect)


my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

single_tickets = [42,4,7,11,1,13]
picks = []
# for i in range(len(my_tickets)):
#     picks.append(lotto_match(single_tickets, my_tickets[i]))

# print(picks)

# print(prime_in(single_tickets))

def prime_(n):
    list_pre = [2, 3, 5, 7, 11]
    if n in list_pre:
        return True
    elif n == 1:
        return False
    else:
        for i in list_pre:
            if n % i == 0:
                return False
    return True


def prime_gen():
    prime = []
    for i in range(1,50):
        if prime_(i):
            prime.append(i)

    return prime


def random_num(max_length,l,u):
    if u-l < max_length:
        return
    
    num_list = []
    for i in range(max_length):
        while True:
            num = random.randint(l,u)
            if num not in num_list:
                if prime_(num):
                    num_list.append(num)
                    break
    return timsort(num_list)


def prime_missed(array1, array2):
    f = 0
    s = 0
    array1 = timsort(array1)
    array2 = timsort(array2)    
    missed_prime = []
    while True:
        if f >= len(array1):
            return missed_prime
        if s >= len(array2):
            missed_prime.extend(array1[f:])
            return missed_prime
        
        if array1[f] == array2[s]:
            f += 1
            s += 1
        elif array1[f] < array2[s]:
            missed_prime.append(array1[f])
            f += 1
        else:
            s += 1
    
    return missed_prime


# ticket = []
# prime = prime_gen()
# for i in range(len(my_tickets)):
#     ticket.extend(my_tickets[i][:])

# print(prime_missed(prime,ticket))

def matched(array1, array2):
    f = 0
    s = 0
    count = 0
    while count < 3:
        if f >= len(array1):
            return False
        if s >= len(array2):
            return False

        if array1[f] == array2[s]:
            count += 1
            f += 1
            s += 1
        elif array1[f] < array2[s]:
            f += 1
        else:
            s += 1
    return True


def experiment():
    count = 1
    while count <= 20:
        draw = random_num(6,1,49)
        for i in range(len(my_tickets)):
            if matched(draw, my_tickets[i]):
                return [draw,my_tickets[i],i,f"found in {count}th draw"]
        count += 1



# result = experiment()
# if len(result) == 4:
#     print("draw", result[0])
#     print(f"{result[2]}th","myticket", result[1])
#     print(result[3])


