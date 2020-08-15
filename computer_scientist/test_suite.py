import sys
from vector import *


def test(result):
    '''
    print the result of a test.
    '''

    line = sys._getframe(1).f_lineno
    if result:
        msg = f"Test at line {line} ok."
    else:
        msg = f"Test at line {line} FAILED."
    print(msg)


test(add_vector([1,1],[1,1]) == [2,2])
test(add_vector([1,2],[1,4]) == [2,6])
test(add_vector([1,2,1],[1,4,3]) == [2,6,4])
print()
test(scalar_mult(5, [1,2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
print()
test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
print()
test(replace('Mississippi', 'i', 'I') == 'MIssIssIppI')
s = 'I love spom! Spom is my favorite food. Spom, spom, yum!'
test(replace(s, 'om', 'am') == 'I love spam! Spam is my favorite food. Spam, spam, yum!')
test(replace(s, 'o', 'a') == 'I lave spam! Spam is my favarite faad. Spam, spam, yum!')
