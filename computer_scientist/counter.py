def count_even_odd(numbers):
    '''
    Count the number of even and odd number.
    '''
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def sum_even_odd(numbers):
    '''
    Sum all the even and odd number.
    '''
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return even, odd


def word_length_5(word_list):
    '''
    Count all the word of length 5.
    '''
    counter = 0
    for i in word_list:
        if len(i) == 5:
            counter += 1
    return counter


def sum_even_except_first(numbers):
    '''
    Sum all the even numbers except first number.
    '''
    count = 0
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
            if count != 1:
                sum += i
    return sum


def count_words_upto_and_including_sam(word_list):
    '''
    Count all the words up to and including the word 'sam'.
    '''
    count = 0
    for i in word_list:
        if i.lower() == "sam":
            count += 1
            return count
        count += 1


def table(n):
    '''
    print the table in paper
    '''
    for i in range (1, n+1):
        for j in range(1, i+1):
            print(i * j, "\t", end="")
        print()


def count_even_digits(n):
    '''
    Counts for even digits i.e 1234565432,
    Ans = 5
    '''
    count = 0
    for i in n:
        if int(i) % 2 == 0:
            count += 1
    return count


def sum_of_squares(n):
    '''
    Sum of squares i.e [2, 3, 4],
    result = 4+9+16
    '''
    sum = 0
    for i in n:
        sum += i ** 2
    return sum


def count_letters(string, Aa):
    '''
    Count the number of alphabet in a string.
    '''
    counter = 0
    index = 0
    index_list = []
    for i in string:
        if i == Aa:
            num = string.find(i, index)
            index = num + 1
            index_list.append(num)
            counter += 1
    return counter, index_list


def clean_string_with_return_details(string, Aa):
    suffix = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    clean_string = ""
    for i in string:
        if i not in suffix:
            clean_string += i
    
    clean_string_list = clean_string.split()
    num_letter = count_letters(clean_string, Aa)[0]
    percent_num_letter = (num_letter/ len(clean_string)) * 100
    return f"Your text contains {len(clean_string_list)} words, of which {num_letter} ({round(percent_num_letter, 2)}%) contain an '{Aa}'"


def reverse(string):
    new_string = ""
    start = len(string) -1
    for i in range(start, -1, -1):
        new_string += string[i]
    return new_string


def mirror(string):
    new_string = ""
    start = len(string) -1
    for i in range(start, -1, -1):
        new_string += string[i]
    return string + new_string


def remove_letter(Aa, string):
    new_string = ""
    for i in string:
        if i != Aa:
            new_string += i
    return new_string


def is_palindrome(string):
    length = len(string) // 2
    rev = reverse(string[:length])
    if len(string) % 2 == 0:
        if string[length:] == rev:
            return True
    else:
        if string[length + 1:] == rev:
            return True


def count_substring(Aa, string):
    count = 0
    for i in range(0, len(string)):
        if Aa == string[i:i+len(Aa)]:
            count += 1
    return count


def remove_substring(Aa, string):
    count = 0
    start = 0
    new_string = ""
    while start < len(string):
        if Aa == string[start:start+len(Aa)]:
            count += 1
            if count == 1:
                start += len(Aa)
        new_string += string[start]
        start += 1
    return new_string


def remove_all_substring(Aa, string):
    count = 0
    start = 0
    new_string = ""
    while start < len(string):
        if Aa == string[start:start+len(Aa)]:
            start += len(Aa)
        else:
            new_string += string[start]
            start += 1
    return new_string


import random
def random_num(num, lower_bound, upper_bound):

    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    The result list cannot contain duplicates.
    """
    range_n = upper_bound - lower_bound
    if range_n < num:
        return
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


def replace_strings(old, new, s):
    list_o = s.split(old)
    list_n = new.join(list_o)
    return list_n


# xs = random_num(10, 1, 11)
# print(xs)

#####################################################################################################

# print(clean_string_with_return_details("""
# We’ll often work with strings that contain punctuation, or tab and newline characters, especially, as we’ll see in a future chapter, when we read our text from files or from the Internet. But if we’re writing a program, say, to count word frequencies or check the spelling of each word, we’d prefer to strip off these unwanted characters.
# We’ll show just one example of how to strip punctuation from a string. Remember that strings are immutable, so we cannot change the string with the punctuation — we need to traverse the original string and create a new string, omitting any punctuation:
# So far we have seen built-in types like int, float, bool, str and we’ve seen lists and pairs. Strings, lists, and pairs are qualitatively different from the others because they are made up of smaller pieces. In the case of strings, they’re made up of smaller strings each containing one character.
# Types that comprise smaller pieces are called compound data types. Depending on what we are doing, we may want to treat a compound data type as a single thing, or we may want to access its parts. This ambiguity is useful.
# So far we have seen built-in types like int, float, bool, str and we’ve seen lists and pairs. Strings, lists, and pairs are qualitatively different from the others because they are made up of smaller pieces. In the case of strings, they’re made up of smaller strings each containing one character.
# Types that comprise smaller pieces are called compound data types. Depending on what we are doing, we may want to treat a compound data type as a single thing, or we may want to access its parts. This ambiguity is useful.
# So far we have seen built-in types like int, float, bool, str and we’ve seen lists and pairs. Strings, lists, and pairs are qualitatively different from the others because they are made up of smaller pieces. In the case of strings, they’re made up of smaller strings each containing one character.
# Types that comprise smaller pieces are called compound data types. Depending on what we are doing, we may want to treat a compound data type as a single thing, or we may want to access its parts. This ambiguity is useful.
# """, "a"))

#####################################################################################################

# print(remove_letter("a", "raman"))

####################################################################################################

# print(is_palindrome(""))

######################################################################################################

# print(count_substring("is", "Mississippi"))
# print(count_substring("an", "banana"))
# print(count_substring("ana", "banana"))
# print(count_substring("nana", "banana"))
# print(count_substring("nanan", "banana"))
# print(count_substring("aaa", "aaaaaa"))

####################################################################################################

# print(remove_substring("an", "banana"))
# print(remove_substring("cyc", "bicycle"))
# print(remove_substring("iss", "Mississippi"))
# print(remove_substring("eggs", "bicycle"))

#####################################################################################################

# print(remove_all_substring("an", "banana"))
# print(remove_all_substring("cyc", "bile"))
# print(remove_all_substring("iss", "Mississippi"))
# print(remove_all_substring("eggs", "bicycle"))


from test_suite import *
print()
test(replace_strings(',', ';', 'this, that, and some other thing') == 'this; that; and some other thing')
test(replace_strings(' ', '**', 'Words will now be separated by stars.') == 'Words**will**now**be**separated**by**stars.')
