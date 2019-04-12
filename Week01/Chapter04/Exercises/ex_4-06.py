# Write a void function draw_equitriangle(t, sz) which calls draw_poly from the previous question to have its turtle
# draw a equilateral triangle.

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

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)


wn = make_window(title="Exercise 1")
alex = make_turtle()

draw_equitriangle(alex, 200)

wn.mainloop()
