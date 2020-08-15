import turtle

def draw_poly(obj, n, angle, length):
    for i in range(n):
        obj.forward(length)
        obj.left(angle)


window = turtle.Screen()
obj = turtle.Turtle()

n = int(window.numinput("Sides", "Number of sides"))
length = window.numinput("Length", "Length of sides")
angle = 360 / n
obj.pensize(2)

draw_poly(obj, n, angle, length)
window.mainloop()