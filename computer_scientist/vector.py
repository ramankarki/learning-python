def add_vector(u, v):
    new_list = []
    if len(u) != len(v):
        return
    else:
        for i in range(len(u)):
            new_list.append(u[i] + v[i])
    return new_list


def scalar_mult(s, v):
    new_list = []
    for i in v:
        new_list.append(i * s)
    return new_list


def dot_product(u, v):
    sum = 0
    if len(u) != len(v):
        return
    else:
        for i in range(len(u)):
            sum = u[i] * v[i] + sum
    return sum


def replace(s, old, new):
    n = s.split(old)
    nr = f"{new}".join(n)
    return nr


def swap(x, y): # incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)


a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)
