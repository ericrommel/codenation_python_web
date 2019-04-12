# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
#     An equilateral triangle
#     A square
#     A hexagon (six sides)
#     An octagon (eight sides)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercise 6")


triangle = turtle.Turtle()
triangle.color("hotpink")
triangle.pensize(3)
for i in range(3):
    triangle.forward(80)
    triangle.left(120)

square = turtle.Turtle()
square.color("hotpink")
square.pensize(4)
for i in range(4):
    square.forward(80)
    square.left(90)

hexagon = turtle.Turtle()
hexagon.color("hotpink")
hexagon.pensize(6)
for i in range(6):
    hexagon.forward(80)
    hexagon.left(60)

octagon = turtle.Turtle()
octagon.color("hotpink")
octagon.pensize(8)
for i in range(8):
    octagon.forward(80)
    octagon.left(45)

wn.mainloop()
