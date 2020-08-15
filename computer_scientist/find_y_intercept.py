
def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    return y1 - (m*x1)


