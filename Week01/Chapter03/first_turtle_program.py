import turtle
bg_color = input("Write a background color for the window: ")
wn = turtle.Screen()
wn.bgcolor(bg_color)
wn.title("Hello, Tess!")

turtle_color = input("Write a color for the turtle: ")
pen_size = int(input("Write a size for the turtle: "))
tess = turtle.Turtle()
tess.color(turtle_color)
tess.pensize(pen_size)

# alex = turtle.Turtle()

# alex.forward(50)
# alex.left(90)
# alex.forward(30)

tess.forward(50)
tess.left(90)
tess.forward(30)

wn.mainloop()
