# Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right
# by 144, put the pen down, and draw the next star. You’ll get something like this:
# 
# _images/five_stars.png
# 
# What would it look like if you didn’t pick up the pen?

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

def draw_star(a_turtle, side=100):
    for i in range(5):
        a_turtle.right(144)
        a_turtle.forward(side)

wn = make_window(title="Exercise 9")
star = make_turtle()

star.penup()
star.setposition(-250, 0)
star.pendown()
star.speed(0)

for j in range(5):
    draw_star(star)
    star.penup()
    star.forward(500)
    star.right(144)
    star.pendown()

star2 = make_turtle(color="red")
star2.penup()
star2.setposition(-100, 0)
star2.pendown()
star2.speed(0)

for j in range(5):
    draw_star(star2)
    star2.forward(150)
    star2.right(144)

wn.mainloop()
