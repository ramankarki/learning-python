import random, time


def linear_sort(array, reverse=False):
    '''
    returns sorted list when reverse is False, returns reverse when reverse is True.
    '''
    numbers = array.copy()
    ascend_numbers = []
    descend_numbers = []

    while len(numbers) != 0:
        small = numbers[0]
        for i in numbers:
            if i < small:
                small = i
        print(small)
        ascend_numbers.append(small)
        numbers.remove(small)

    if reverse:
        for i in range(len(ascend_numbers)-1, -1, -1):
            descend_numbers.append(ascend_numbers[i])
        return descend_numbers
    return ascend_numbers


def remove_dupli(values):
    values.sort()
    new_list = []
    recent_value = None
    for i in values:
        if recent_value != i:
            new_list.append(i)
            recent_value = i
    return new_list


def _sort():
    array = [7,3,4,7,3]
    sort = []
    for i in range(len(array)):
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
    return array


def merge_A_intersection_B(array1, array2):
    '''
    merge any two list using set (A^B) formula,
    conditions: * list should be sorted
                * no duplicate element
    '''
    f = 0
    s = 0
    list1 = array1.copy()   # avoiding side effect
    list2 = array2.copy()
    list1.sort()
    list2.sort()
    print("first list:", list1)
    print("second list:", list2)
    new_list = []
    while True:
        if f >= len(list1):             # if first list is finished,
            return new_list             # we're done
        if s >= len(list2):             # same again
            return new_list

        if list1[f] == list2[s]:        # if equal, 
            new_list.append(list1[f])   # they are same
            f += 1                      # go for next element of both
            s += 1                      
        elif list1[f] < list2[s]:       # if less, then there is no chance of being equal with another element of second list
            f += 1                      # so compare next element of first list with same element of second list
        else:
            s += 1                      # same again

 
def merge_A_minus_B(array1, array2):
    '''
    merge any two list using set (A-B) formula,
    conditions: * list should be sorted
                * no duplicate element
    '''
    f = 0
    s = 0
    list1 = array1.copy()         # avoiding side effect
    list2 = array2.copy()
    list1.sort()  
    list2.sort()
    print("first list:", list1)    
    print("second list:", list2)
    
    new_list = []

    while True:
        if f >= len(list1):             # if first list is finished,
            new_list.extend(list1[f:])  # we're done.
            return new_list
        if s >= len(list2):             # same again
            new_list.extend(list1[f:])
            return new_list

        if list1[f] == list2[s]:        # if both element are same
            f += 1                      # go for next element both
            s += 1
        elif list1[f] < list2[s]:       # if first list's element is small,
            new_list.append(list1[f])   # then there no chance it will occur in next element of second list
            f += 1                      # so, it is only in first list and can be appended
        else:                           
            s += 1                      # if greater, then is may occur in next element of second list


def merge_A_u_B_minus_intersection(array1, array2):
    '''
    merge any two list using set (AuB)-(AnB) formula,
    conditions: * list should be sorted
                * no duplicate element
    '''
    list1 = array1.copy()
    list2 = array2.copy()
    list1.sort()
    list2.sort()
    print("first list:", list1)
    print("second list:", list2)
    f = 0
    s = 0
    new_list = []
    while True:
        if f >= len(list1):
            new_list.extend(list2[s:])
            return new_list
        if s >= len(list2):
            new_list.extend(list1[f:])
            return new_list

        if list1[f] == list2[s]:
            f += 1
            s += 1
        elif list1[f] < list2[s]:
            new_list.append(list1[f])
            f += 1
        else:
            new_list.append(list2[s])
            s += 1
    


# num_list = []
# for i in range(100000):
#     num = random.randint(1, 100000)
#     num_list.append(num)

# print(num_list[:10])
# t0 = time.time()
# print(sort(num_list)[:10])
# t1 = time.time()
# print("time taken:", t1-t0)
# print(insertion_sort())


def generate(): # generating 10 unique numbers from 1-20
    l1 = []
    for i in range(10):
        while True:
            num = random.randint(1,20)
            if num not in l1:
                break
        l1.append(num)
    return l1

# for i in range(1,11):   # testing
#     l1 = generate()
#     l2 = generate()
#     print("#############", i, "###############")
#     print(merge_A_u_B_minus_intersection(l1,l2))
#     print()
    
print(merge_A_minus_B([5,7,11,11,11,12,13],[7,8,11]) == [5,11,11,12,13])
