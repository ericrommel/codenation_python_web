import turtle
import time

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

def draw_poly(t, n, sz):
    t.pendown()
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
    t.penup()

wn = make_window(title="Chapter 05")
alex = make_turtle(pensize=5, color="black")

# We can get a turtle to display text on the canvas at the turtle’s current position. The method to do that is:
alex.write("Hello")

time.sleep(3)

alex.penup()
alex.setposition(-250, 150)
alex.pendown()
# We can fill a shape (circle, semicircle, triangle, etc.) with a color. It is a two-step process.
# First we call the method:
alex.begin_fill()
# then we draw the shape
draw_poly(alex, 3, 100)
# then we call
alex.end_fill()

alex.penup()
alex.setposition(50, 150)
alex.pendown()
# We’ve previously set the color of our turtle — we can now also set its fill color, which need not be the same as
# the turtle and the pen color. We use
alex.color("blue", "red")
alex.begin_fill()
draw_poly(alex, 6, 100)
alex.end_fill()

# Ok, so can we get tess to draw a bar chart? Let us start with some data to be charted,
xs = [48, 117, 200, 240, 160, 260, 220]

# Corresponding to each data measurement, we'll draw a simple rectangle of that height, with a fixed width.
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

tess = make_turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

tess.penup()
tess.setposition(-250, -300)
tess.pendown()
for v in xs:              # Assume xs and tess are ready
    draw_bar(tess, v)


wn.mainloop()
