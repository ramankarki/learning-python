import turtle 

# setup window and turtle
window = turtle.Screen()
obj = turtle.Turtle()

# setup prompt 
window.title("Hello, turtle!")
color = window.textinput("Screen", "background color (rgb format, hexa decimal code or color name)")
pen_color = window.textinput("Pen color", "pen color")
width = window.numinput("Pen size", "pensize width (recommended max: 5)")

# setup input from user
window.bgcolor(color)
obj.color(pen_color)
obj.pensize(width)

# setup turtle angle
obj.forward(50)
obj.left(120)
obj.forward(50)

# wait until user closes window
window.mainloop()