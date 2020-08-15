import time

sum = 0
t0 = time.time()
for i in range(100001):
    sum += i

t1 = time.time()
print(t1-t0)

sum = 0
t0 = time.time()
sum = (100000 * (100000+1)) / 2
t1 = time.time()
print(t1-t0)
