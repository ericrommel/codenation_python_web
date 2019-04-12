# Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image shown below. Assume each
# side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when
# the program ends.)
# _images/five_squares.png
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


wn = make_window(title="Exercise 1")
alex = make_turtle()

for j in range(5):
    draw_square(alex)
    alex.penup()
    alex.forward(40)

wn.mainloop()
