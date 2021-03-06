# Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.

import turtle

def make_window(color="lightgreen", title="Exercise"):
    win = turtle.Screen()
    win.bgcolor(color)
    win.title(title)
    return win

def make_turtle(pensize=3, color="yellow"):
    a_turtle = turtle.Turtle()
    a_turtle.color(color)
    a_turtle.pensize(pensize)
    return a_turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.penup()
    t.forward(10)
    t.pendown()

wn = make_window(title="Exercise 07")
tess = make_turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for v in xs:              # Assume xs and tess are ready
    draw_bar(tess, v)


wn.mainloop()
