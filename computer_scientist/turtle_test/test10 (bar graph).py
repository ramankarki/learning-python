import turtle

def bar(obj, height, color):
    obj.color(color)
    obj.begin_fill()
    obj.left(90)
    obj.forward(height)
    obj.right(90)
    obj.write(" " * 4 + str(height))
    obj.forward(40)
    obj.right(90)
    obj.forward(height)
    obj.end_fill()
    obj.left(90)
    obj.penup()
    obj.forward(10)
    obj.pendown()


def bar_color(num):
    if num >= 200:
        return "red"
    elif num >= 100 and num < 200:
        return "yellow"
    elif num < 100:
        return "green"


window = turtle.Screen()
obj = turtle.Turtle()

for i in [-200, -10, 48, 117, 200, 240, 160, 260, 220]:
    color = bar_color(i)
    bar(obj, i, color)

obj.hideturtle()
window.mainloop()