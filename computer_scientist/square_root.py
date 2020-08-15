def sqroot(n):
    aprox = n/2.0
    record = []
    while True:
        better = (aprox + n/aprox) / 2
        record.append(better)
        if abs(better-aprox) < 0.001:
            return record
        aprox = better


record = sqroot(8)
for i in record:
    if record.index(i) == len(record) - 1:
        print("Final aprox:", i)
    else:
        print(i)

