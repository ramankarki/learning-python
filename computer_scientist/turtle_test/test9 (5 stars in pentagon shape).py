import turtle

window = turtle.Screen()
obj = turtle.Turtle()

def star(obj, length):
    for i in range(5):
        obj.forward(length)
        obj.right(144)


obj.pensize(2)
angle = 72
for i in range(5):
    obj.penup()
    obj.forward(150)
    obj.pendown()
    obj.setheading(0)
    star(obj, 100)
    obj.setheading(angle)
    angle += 72

window.mainloop()