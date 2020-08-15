# import turtle           # Tess becomes a traffic light.

# turtle.setup(400,500)
# wn = turtle.Screen()
# wn.title("Tess becomes a traffic light!")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()


# def draw_housing():
#     """ Draw a nice housing to hold the traffic lights """
#     tess.pensize(3)
#     tess.color("black", "darkgrey")
#     tess.begin_fill()
#     tess.forward(80)
#     tess.left(90)
#     tess.forward(200)
#     tess.circle(40, 180)
#     tess.forward(200)
#     tess.left(90)
#     tess.end_fill()


# draw_housing()

# tess.penup()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
# # Turn tess into a big green circle
# tess.shape("circle")
# tess.shapesize(3)
# tess.fillcolor("green")

# # A traffic light is a kind of state machine with three states,
# # Green, Orange, Red.  We number these states  0, 1, 2
# # When the machine changes state, we change tess' position and
# # her fillcolor.

# # This variable holds the current state of the machine
# state_num = 0


# def advance_state_machine():
#     global state_num
#     if state_num == 0:       # Transition from state 0 to state 1
#         tess.forward(70)
#         tess.fillcolor("orange")
#         state_num = 1
#     elif state_num == 1:     # Transition from state 1 to state 2
#         tess.forward(70)
#         tess.fillcolor("red")
#         state_num = 2
#     else:                    # Transition from state 2 to state 0
#         tess.back(140)
#         tess.fillcolor("green")
#         state_num = 0
#     wn.ontimer(advance_state_machine, 3000)


# # Bind the event handler to the space key.
# # wn.onkey(advance_state_machine, "space")
# wn.ontimer(advance_state_machine, 3000)

# wn.listen()                      # Listen for events
# wn.mainloop()


#################################################################################################
                              # alternate method #
#################################################################################################


import turtle       # Tess becomes a traffic light.
import time


turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
red = turtle.Turtle()
orange = turtle.Turtle()
green = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.hideturtle()

# Position tess onto the place where the green light should be
for i in [red, orange, green]:
    i.forward(40)
    i.left(90)

for l,obj in [(50, green), (120, orange), (190, red)]:
    obj.penup()
    obj.forward(l)
    obj.shape("circle") # Turn tess into a big green circle
    obj.shapesize(3)
    obj.fillcolor("white")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine


def advance_state_machine(color1, color2, color3, t):
    red.fillcolor(color1)
    orange.fillcolor(color2)
    green.fillcolor(color3)
    time.sleep(t)

# Bind the event handler to the space key.
# wn.onkey(advance_state_machine, "space")
while True:
    for t,color1,color2,color3 in [(3, "green", "white", "white"), (1, "green", "orange", "white"), (1, "white", "orange", "white"), (2, "white", "white", "red")]:
        advance_state_machine(color1, color2, color3, t)

wn.listen()                      # Listen for events
wn.mainloop()
