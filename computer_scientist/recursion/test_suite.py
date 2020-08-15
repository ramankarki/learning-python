import sys


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


