import turtle, time


def pg110_12():
    '''
    Draw this shape without lifting pen.

     /\.
    /  \.
   ------
   |\  /|
   | \/ |
   | /\ |
   |/  \|
   ------

    '''
    experiment = [(0, 100), (135, 141.42), (135, 100), (135, 141.42), (135, 100), (-120, 100), (-120, 100), (-30, 100)]
    for x,y in experiment:
        obj.left(x)
        obj.forward(y)
        time.sleep(0.5)


def pg110_13_a():
    '''
    Draw this shape without lifting pen.
     /\.
    /  \.
   ------
   |    |
   |    |
   ------

    '''
    experiment = [(60, 100), (-120, 100), (-120, 100), (90, 100), (90, 100), (90, 100)]
    for x,y in experiment:
        obj.left(x)
        obj.forward(y)
        time.sleep(0.5)


def pg110_13_b():
    '''
    Draw this shape without lifting pen.
     /\.
    /  \.
   ------
   |\   |
   | \  |
   |  \ |
   ------

    '''
    experiment = [(135, 141.42), (135, 100), (90, 100), (90, 100), (90, 100), (-120, 100), (-120, 100)]
    for x,y in experiment:
        obj.left(x)
        obj.forward(y)
        time.sleep(0.5)


def pg110_13_c():
    '''
    Draw this shape without lifting pen.
     /\.
    /  \.
   ------
   |    |
   |    |
   ------

    '''
    experiment = [(60, 100), (-120, 100), (-120, 100), (90, 100), (90, 100), (90, 100)]
    for x,y in experiment:
        obj.left(x)
        obj.forward(y)
        time.sleep(0.4)


def pg110_13_e():
    '''
    Draw this shape without lifting pen.
          /\.
         /  \.
        /    \.
       /------\.
      / |    | \.
     /  |    |  \.
     \  |    |  /
      \ |    | /
       \------/

    '''
    experiment = [(150, 100), (-120, 100), (30, 100), (-120, 100), (30, 100), (-120, 100), (-30, 100), (-90,100), (-90, 100), (-90, 100)]
    for x,y in experiment:
        obj.left(x)
        obj.forward(y)
        time.sleep(0.4)


def pg110_13_f():
    '''
    Draw this shape without lifting pen.
          /\.
         /  \.
        /    \.
       /------\.
      / |\  /| \.
     /  | \/ |  \.
     \  | /\ |  /
      \ |/  \| /
       \------/

    '''
    experiment = [(225, 141.42), (-75, 100), (-120, 100), (30, 100), (-120, 100), (30, 100), (-120, 100), (-75, 141.42), (135, 100), (90, 100), (90, 100), (90, 100)]
    for x,y in experiment:
        obj.left(x)
        obj.forward(y)
        time.sleep(0.4)


window = turtle.Screen()
obj = turtle.Turtle()
obj.pensize(2)

pg110_13_f()

obj.hideturtle()
window.mainloop()
