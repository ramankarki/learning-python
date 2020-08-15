import time

def linear_remove_dipli(values):
    values.sort()
    new_list = []
    recent_value = None
    for i in values:
        if recent_value != i:
            new_list.append(i)
            recent_value = i
    return new_list


def linear_search(word_list, word):
    '''
    index of word from word_list
    '''
    for i,w in enumerate(word_list):
        if w == word:
            return i
    return -1


def linear_sort(array, reverse=False):  # slow sorting
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


def timsort(array):
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


def text_to_words(the_text):
    """ 
    return a list of words with all punctuation removed,
    and all in lowercase
    """
    txt = the_text.split()
    wds = []
    for i in txt:
        wds.append(i.lower())

    clean_wds = []
    trash = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "_", "=", "{", "}", "[", "]", "\\", "|", ":", ";", "'", '"', "<", ",", ">", ".", "/", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for word in wds:
        string = ""
        for letter in word:
            if letter not in trash:
                string += letter
        if len(string) > 1:
            clean_wds.append(string)
    # clean_wds = removing_diplicates(clean_wds) # it took 1 sec more
    clean_wds = set(clean_wds)
    clean_wds = list(clean_wds)
    clean_wds = sorted(clean_wds)
    return clean_wds


def load_vocab(file_name):
    '''
    load vocabulary file and extract words by cleaning it
    '''
    myfile = open(file_name, "r")
    content = myfile.read()
    myfile.close()
    words = text_to_words(content)
    print("Vocabulary loaded.")
    return words


def get_words_in_book(file_name):
    '''
    load words from book by cleaning it
    '''
    myfile = open(file_name, "r")
    content = myfile.read()
    myfile.close()
    words = text_to_words(content)
    print("Book loaded.")
    return words


def binary_search(vocab, word):
    '''
    find and return the index of key in sequence vocab.
    '''
    lb = 0
    ub = len(vocab) - 1
    mid_index = 0

    while True:
        if lb == ub: # empty string is always less than strings, it ends when ub is 0 and ends the region fo interest (ROI)
            return -1

        mid_index = (lb + ub) // 2 # next probe should be in the middle of ROI and also contains the index of word from vocabularly
        item = vocab[mid_index]
        print(f"ROI [{lb}:{ub}], probed='{item}', target='{word}'")

        if item == word:
            return mid_index
        if word > item:       # if word is in top half
            lb = mid_index + 1
        else:                 # if word is in bottom half
            ub = mid_index


def find_unknown_merge_pattern(vocab, word_list): # using merge pattern
    '''
    returns unknown words from the word_list.
    '''
    vocab = load_vocab(vocab)
    word_list = get_words_in_book(word_list)
    result = []
    f = 0
    s = 0
    while True:
        if f >= len(word_list):
            return result
        if s >= len(vocab):
            return result
        
        if word_list[f] == vocab[s]:
            f += 1
            s += 1
        elif word_list[f] < vocab[s]:   # if it is less than vocab word,
            result.append(word_list[f]) # then is has no chance to appear in next element in vocabularly
            f += 1
        else:
            s += 1
        
    return result


def find_unknown_words(vocab, word_list): # using binary search
    '''
    returns unknown words from the word_list.
    '''
    vocab = load_vocab(vocab)
    word_list = get_words_in_book(word_list)
    result = []
    for i in word_list:
        if binary_search(vocab, i) < 0:
            result.append(i)
    return result


if __name__ == "__main__":
    import time, random

    # loading book and vocabularly 
    # t0 = time.time()
    # print("Unknown words:",len(find_unknown_merge_pattern("vocab.txt", "download.txt")))
    # t1 = time.time()
    # print(t1-t0)


    # tim sorting algorithm
    num_list = []
    for i in range(100000):
        num = random.randint(1, 10000000)
        num_list.append(num)

    print(num_list[:10])
    t0 = time.time()
    print(timsort(num_list)[:10])
    t1 = time.time()
    print("time taken:", t1-t0)




