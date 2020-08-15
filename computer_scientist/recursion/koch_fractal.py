def snow_flake(t, n, size):
    if n > 0:
        if n == 0:
            t.forward(size)
        else:
            for i in range(3):
                koch(t, n-1, size/3)
                t.left(-120)


def koch(t, n, size):
    if n > 0:
        if n == 0:
            t.forward(size)
        else:
            for i in [60, -120, 60, 0]:
                koch(t, n-1, size/3)
                t.left(i)


import turtle

window = turtle.Screen()
obj = turtle.Turtle()

snow_flake(obj, 6, 400)

window.mainloop()

