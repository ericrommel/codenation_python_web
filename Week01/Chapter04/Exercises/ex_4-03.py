# Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. When called with
# draw_poly(tess, 8, 50), it will draw a shape like this:
# 
# _images/regularpolygon.png

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


def draw_poly(t, n, sz):
    t.pendown()
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
    t.penup()


wn = make_window(title="Exercise 2")
tess = make_turtle()
draw_poly(tess, 8, 50)

wn.mainloop()
