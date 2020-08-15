import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
size = 1
# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def red():
    tess.color("red")

def green():
    tess.color("green")

def blue():
    tess.color("blue")

def width_increase():
    global size
    if size < 20:
        size += 1
    tess.pensize(size)

def width_decrease():
    global size
    if size > 1:
        size -= 1
    tess.pensize(size)

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(red, "r")
wn.onkey(green, "g")
wn.onkey(blue, "b")
wn.onkey(width_increase, "KP_Add")
wn.onkey(width_decrease, "KP_Subtract")


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

