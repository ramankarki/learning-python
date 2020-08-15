def merge(array, l, mid, r):
    left = array[l:mid+1]
    right = array[mid+1:r+1]

    i = 0
    j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def partition(array, left, right):
    if left < right:
        mid = (left+right) // 2
        partition(array, left, mid)
        partition(array, mid+1, right)
        merge(array, left, mid, right)


def merge_sort(array):
    partition(array, 0, len(array)-1)


if __name__ == "__main__":
    import time, random

    # merge sorting algorithm
    num_list = [1,0,2]
    for i in range(1000000):
        num = random.randint(1, 10000000)
        num_list.append(num)

    print(num_list[:10])
    t0 = time.time()
    merge_sort(num_list)
    t1 = time.time()
    print(num_list[:10])
    print("time taken:", t1-t0)


