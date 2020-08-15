import turtle

window = turtle.Screen()
obj = turtle.Turtle()

def square(obj, length):
    for j in range(4):
        obj.forward(length)
        obj.left(90)


obj.pensize(2)
size = 20
for i in range(5):
    square(obj, size)
    obj.penup()
    obj.backward(10)
    obj.right(90)
    obj.forward(10)
    obj.left(90)
    obj.pendown()
    size += 20

window.mainloop()