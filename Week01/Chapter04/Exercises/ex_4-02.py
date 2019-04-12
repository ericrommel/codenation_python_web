# Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20
# units bigger, per side, than the one inside it.
# 
# _images/nested_squares.png
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

def draw_square(a_turtle, side=20):
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(side)
        a_turtle.left(90)
    a_turtle.penup()


wn = make_window(title="Exercise 2")
alex = make_turtle()

for j in range(1, 6):
    draw_square(a_turtle=alex, side=20*j)
    alex.penup()
    alex.left(-180)
    for k in range(2):
        alex.forward(10)
        alex.left(90)

wn.mainloop()
