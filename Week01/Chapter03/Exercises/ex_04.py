# Suppose our turtle tess is at heading 0 — facing east.
# We execute the statement tess.left(3645).
# What does tess do, and what is her final heading?

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Heading")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

tess.forward(80)
tess.left(3645)
tess.forward(80)

wn.mainloop()

