result = "{0:>4} {1:>6} {2:>8} {3:>8} {4:>11}"
print(result.format("i", "i**2", "i**3", "i**4", "i**5"))
for i in range(1, 11):
    print(result.format(i, i**2, i**3, i**4, i**5))