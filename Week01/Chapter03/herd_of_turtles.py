import turtle
# bg_color = input("Write a background color for the window: ")
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess and Alex")

# turtle_color = input("Write a color for the turtle: ")
# pen_size = int(input("Write a size for the turtle: "))
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()

# Make Tess draw equilateral triangle
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
# Complete the triangle

tess.right(180)  # Turn Tess around
tess.forward(80)  # Move her away from the origin

# Make Alex draw a square
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
