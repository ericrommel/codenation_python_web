# In the turtle bar chart program, what do you expect to happen if one or more of the data values in the list is
# negative? Try it out. Change the program so that when it prints the text value for the negative bars,
# it puts the text below the bottom of the bar.

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
    t.penup()

    if height < 0:
        t.forward(-17)
    t.write("  " + str(height))
    if height < 0:
        t.forward(17)
    
    t.pendown()
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

xs = [48, 117, 200, -50, 240, 160, 260, 220]

for v in xs:              # Assume xs and tess are ready
    if v >= 200:
        tess.color("blue", "red")
    elif v >= 100 and v < 200:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")
    draw_bar(tess, v)


wn.mainloop()
