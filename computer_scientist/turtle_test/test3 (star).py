import turtle

window = turtle.Screen()
obj = turtle.Turtle()

obj.pensize(3)
obj.left(72)
for i in range(5): # angle of corner of star is 36 degree and pentagon is 108 degree
    obj.forward(100)
    obj.right(144)

obj.hideturtle()
window.mainloop()