import random
import time

result = []
for i in range(10):
    count = 0
    flip = 0
    while count < 100:
        count +=1
        if random.randint(0, 1) == 1:
            flip += 1
    result.append(flip)

print(result) #flipping 10 times to see different results
print(max(result))
print(min(result))

