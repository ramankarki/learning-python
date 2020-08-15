def insertion_sort(array):
    '''
    sort any list
    '''
    copy_array = array.copy()
    for i in range(1, len(copy_array)):
        current = copy_array[i]
        while copy_array[i-1] > current and i >= 1:
            copy_array[i-1], copy_array[i] = copy_array[i], copy_array[i-1]
            i -= 1
    return copy_array


def merge(list1, list2):
    '''
    merge any two sorted list
    '''
    fl = 0          # first list value carrier
    sl = 0          # second list value carrier
    new_list = []
    while True:
        if fl >= len(list1):                # if list1 is now empty then
            new_list.extend(list2[sl:])     # append all the remaining items from list2
            return new_list                 # we're done
        if sl >= len(list2):                # same again, but swap roles
            new_list.extend(list1[fl:])
            return new_list

        # both list still have some value and are appended one by ony whichever is small
        if list1[fl] <= list2[sl]:
            new_list.append(list1[fl])
            fl += 1
        else:
            new_list.append(list2[sl])
            sl += 1


def tim_sort(array):
    '''
    sorts array and returns a copy
    '''
    copy_array = array.copy()
    step = 16

    for i in range(0, len(copy_array), step):
        copy_array[i:i+step] = insertion_sort(copy_array[i:i+step])

    if len(array) <= step:
        return copy_array

    while step < len(copy_array):
        for i in range(0, len(copy_array), step * 2):
            copy_array[i:i+step * 2] = merge(copy_array[i:i+step], copy_array[i+step:i+step*2])
        step *= 2

    return copy_array


if __name__ == "__main__":
    import time, random

    # tim sorting algorithm
    num_list = []
    for i in range(1000000):
        num = random.randint(1, 1000000)
        num_list.append(num)

    print(num_list[:10])
    t0 = time.time()
    print(tim_sort(num_list)[:10])
    t1 = time.time()
    print("time taken:", t1-t0)

