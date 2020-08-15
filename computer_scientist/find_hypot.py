
def find_hypot(side1, side2):
    exp = round((side1**2 + side2**2) ** 0.5, 1)
    return exp


if __name__ == "__main__":
    length = (input("enter any two side of right_angled triangle: "))
    length = length.split()
    exp = find_hypot(int(length[0]), int(length[1]))
    print(exp)