import turtle
import time

# setup window, turtle, color
window = turtle.Screen()

# obj1 = turtle.Turtle()
# obj1.color("#29cf55")

# obj2 = turtle.Turtle()
# obj2.color("#2a2191")

# obj3 = turtle.Turtle()
# obj3.color("red")

# obj4 = turtle.Turtle()
# obj4.color("yellow")

# obj5 = turtle.Turtle()
# obj6 = turtle.Turtle()

# # turtle motion
# obj1.forward(50)
# obj2.backward(25)
# obj1.left(45)
# obj1.forward(50)


# # move turtle to absolute position with cordinates
# obj3.setpos(50, 0)
# obj3.setpos(50, -50)
# obj3.setpos(0, -50)
# obj3.setpos(0, 0)


# # move turtle to individual cordinate with x or y cordinate
# obj4.setx(40)
# obj4.sety(100)


# # bring back the turtle to origin
# obj5.home()


# # set the angle like the protecter (the principle axis will be same in all position of the turtle)
# obj6.forward(100)
# obj6.right(90)
# obj6.forward(100)
# obj6.setheading(90)


# obj7 = turtle.Turtle()
# obj7.setheading(108)
# obj7.circle(120, 360, 5) # radius, degree from the principle axis, steps


# drawing a star
# obj8 = turtle.Turtle()
# angle = 72
# obj8.setheading(36)
# for i in range(5):
#     obj8.forward(150)
#     obj8.left(144)
#     # obj8.setheading(angle)
#     angle += 72


# draw a dot
# obj9 = turtle.Turtle()
# obj9.dot(50, "blue")   # radius, color


# undo what is done
# obj10 = turtle.Turtle()
# obj10.color("blue")
# obj10.fd(50)
# time.sleep(2)
# obj10.undo()


# turtle.towards(0, 0) returns the angle between the turtle position and position set by method


# 
# turtle.penup()
# turtle.pendown()
# turtle.pensize()
# turtle.width()
# turtle.pencolor("red")  # outer color of pen and color of lines are red
# turtle.fillcolor("blue") # turtle color id filled with blue

# turtle.clear() # clear the drawing without moving the turtle
# turtle.hideturtle() # hide turtle
# turtle.write("Home", False, "center", font=("arial", 25, "italic"))  write 
# turtle.forward(100)


# turtle.shape("arrow") #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
# turtle.forward(100)
# turtle.resizemode("auto")
# turtle.turtlesize(5, 5, 12)
# turtle.shearfactor(1) # cut the turtle


# turtle.shape("square")
# turtle.shapetransform(4, -1, 0, 2)
# print(turtle.get_shapepoly())
# turtle.forward(100)

# def turn(x,y):
#     turtle.left(180)

# def reverse(x,y):
#     turtle.left(180)
# # turtle.onclick(turn)
# # turtle.onrelease(reverse)
# turtle.ondrag(turtle.goto)


               # Screen methods


# turtle.title(titlestring)
# turtle.numinput(title, prompt, default=None, minval=None, maxval=None)
# turtle.textinput(title, prompt)
# turtle.ontimer(fun, t=0) Install a timer that calls fun after t milliseconds.
# turtle.bgpic(picname=None)
# turtle.bgcolor
# window.mainloop()


# from turtle import Turtle, Screen

# TURTLE_SIZE = 20

# screen = Screen()

# yertle = Turtle(shape="turtle", visible=False)
# yertle.penup()
# yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
# yertle.pendown()
# yertle.showturtle()

# screen.mainloop()