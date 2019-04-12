# Draw this pretty pattern.
# _images/tess08.png

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

def draw_square(a_turtle, side=200):
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(side)
        a_turtle.left(90)
    a_turtle.penup()


wn = make_window(title="Exercise 1")
alex = make_turtle()

size = 45
for k in range(0, 200, 45):

    for j in range(4):
        alex.speed(0)
        draw_square(alex)
        alex.penup()
        alex.right(size+k)

wn.mainloop()
