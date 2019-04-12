# If you were going to draw a regular polygon with 18 sides, what angle would you need to turn the turtle at each corner?

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercise 9")

polygon = turtle.Turtle()
polygon.color("red")
polygon.pensize(3)

sides = 18
polygon_sides = 360/sides

polygon.up()
polygon.left(90)
polygon.forward(300)
polygon.right(90)
polygon.down()
for i in range(sides):
    polygon.forward(100)
    polygon.right(polygon_sides)


wn.mainloop()
