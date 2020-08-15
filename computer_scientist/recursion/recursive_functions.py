from test_suite import *

# returns maximum value from array and sub-arrays
def find_max(array):
    largest = None
    first_time = True
    for element in array:
        if type(element) == type([]):
            value = find_max(element)
        else:
            value = element
        
        if first_time:
            largest = value
            first_time = False
        else:
            if value > largest:
                largest = value
    return largest


# returns minimum
def find_min(array):
    lowest = None
    first_time = True
    for element in array:
        if type(element) == type([]):
            value = find_min(element)
        else:
            value = element
        
        if first_time:
            lowest = value
            first_time = False
        else:
            if value < lowest:
                lowest = value

    return lowest


# counts the total number of target within array and sub-array
def count(target, array):
    sum = 0
    for element in array:
        if type(element) == type([]):
            sum += count(target, element)
        else:
            if element == target:
                sum += 1

    return sum


# returns a single array containing all the element of array and sub-array
def flatten(array, condition=True):
    new_list = []
    for element in array:
        if type(element) == type([]):
            new_list.extend(flatten(element))
        else:
            new_list.append(element)
    
    return new_list


def fib(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        a,b = b,a+b
    return a


print(fib(5))


