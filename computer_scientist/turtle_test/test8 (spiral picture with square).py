import turtle

window = turtle.Screen()
obj = turtle.Turtle()

size = 5
for i in range(5):
    obj.forward(size)
    obj.left(90)
    size += 5

for i in range(95):
    obj.forward(size)
    obj.left(91)
    size += 5

window.mainloop()