def cesaro_box(t, n, size):
    if n >= 0:
        for i in range(4):
            cesaro_fractal(t, n-1, size/4)
            t.left(-90)


def cesaro_fractal(t, n, size):
    if n >= 0:
        if n == 0:
            t.forward(size)
        else:
            for i in [-85, 170, 275, 0]:
                cesaro_fractal(t, n-1, size/3)
                t.left(i)



import turtle

window = turtle.Screen()
obj = turtle.Turtle()

cesaro_box(obj, 4, 3000)

window.mainloop()

