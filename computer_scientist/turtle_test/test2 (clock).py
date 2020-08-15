import turtle

window = turtle.Screen()
obj = turtle.Turtle()

obj.penup()
for i in range(12):
    obj.stamp()
    obj.forward(100)
    obj.stamp()
    obj.backward(100)
    obj.left(30)

window.mainloop()