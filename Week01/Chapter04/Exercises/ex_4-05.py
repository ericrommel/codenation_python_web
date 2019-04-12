# The two spirals in this picture differ only by the turn angle. Draw both.
# _images/tess_spirals.png

import turtle

def make_window(color="lightgreen", title="Exercise"):
    win = turtle.Screen()
    win.bgcolor(color)
    win.title(title)
    return win

def make_turtle(pensize=3, color="blue"):
    a_turtle = turtle.Turtle()
    a_turtle.color(color)
    a_turtle.pensize(pensize)
    return a_turtle

def draw_spiral(a_turtle, turn=90, side=2):
    a_turtle.forward(side * 4)
    a_turtle.right(turn)

wn = make_window(title="Exercise 5")
alex = make_turtle()
alex.penup()
alex.setposition(-280, 0)
alex.pendown()
alex.speed(0)

for i in range(92):
    draw_spiral(alex, side=i)

tess = make_turtle()
tess.penup()
tess.setposition(200, 0)
tess.pendown()
tess.speed(0)

for i in range(100):
    draw_spiral(tess, turn=89, side=i)

wn.mainloop()
