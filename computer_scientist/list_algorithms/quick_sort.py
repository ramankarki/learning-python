def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()

    highest = []
    lowest = []
    for i in array:
        if i < pivot:
            lowest.append(i)
        else:
            highest.append(i)
    
    return quick_sort(lowest) + [pivot] + quick_sort(highest)


if __name__ == "__main__":
    import time, random

    # tim sorting algorithm
    num_list = []
    for i in range(1000000):
        num = random.randint(1, 1000000)
        num_list.append(num)

    print(num_list[:10])
    t0 = time.time()
    print(quick_sort(num_list)[:10])
    t1 = time.time()
    print("time taken:", t1-t0)

