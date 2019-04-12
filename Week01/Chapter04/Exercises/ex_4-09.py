# Write a void function to draw a star, where the length of each side is 100 units. (Hint: You should turn the turtle
# by 144 degrees at each point.)
#
#      _images/star.png 

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

draw_star(star)


wn.mainloop()
