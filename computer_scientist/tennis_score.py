# score = []
# for i in range(1, 22):
#     score.append([])
#     for j in range(i):
#         score[i-1].append((0,0))

# for i in score:
#     for j in i:
#         print(j, end="")
#     print()


import random

a = 0
b = 0

for i in range(20):
    toss = random.randint(0, 1)
    if toss == 0:
        a += 15
    else:
        b += 15
    print((a, b))

if a == b:
    print("Draw")
elif a > b:
    print("A won with", a, "points")
else:
    print("B won with", b, "points")