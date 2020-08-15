import turtle

def square(obj, length):
    for i in range(4):
        obj.forward(length)
        obj.left(90)


window = turtle.Screen()
obj = turtle.Turtle()

obj.pensize(2)
for i in range(20):
    square(obj, 100)
    obj.left(18)

window.mainloop()