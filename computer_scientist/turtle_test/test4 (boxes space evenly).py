import turtle

window = turtle.Screen()
obj = turtle.Turtle()

def square(turtle_object, length):
    for i in range(4):
        turtle_object.forward(length)
        turtle_object.left(90)


obj.pensize(2)
for i in range(5):
    square(obj, 20)
    obj.penup()
    obj.forward(40)
    obj.pendown()

window.mainloop()