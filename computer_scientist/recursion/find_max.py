from test_suite import *





print(find_max([[12],3,[4,5,10],7,8,9,[1,100]]) == 100)
test(find_max([2, 9, [1, 13], 8, 6]) == 13)
test(find_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
test(find_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
test(find_max(["joe", ["sam", "ben"]]) == "sam")

test(find_max([2, 9, [1, 13], 8, 6]) == 1)
test(find_max([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(find_max([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(find_max([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

