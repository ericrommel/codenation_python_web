# Write a program to draw a face of a clock that looks something like this:
#
#     _images/tess_clock1.png  
#

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.pensize(5)

size = 250

tess.up()
tess.stamp()
for i in range(12):
    tess.setposition(0, 0)
    tess.right(30)
    tess.forward(size/2)
    tess.down()
    tess.forward(size/20)
    tess.up()
    tess.forward(size/10)
    tess.stamp()

wn.mainloop()

