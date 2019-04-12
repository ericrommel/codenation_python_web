# Enhance your program above to also tell us what the drunk pirate’s heading is after he has finished stumbling around.
# (Assume he begins at heading 0).

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercise 8")

drunk_pirate = turtle.Turtle()
drunk_pirate.color("red")
drunk_pirate.pensize(3)

step = 100
turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in turns:
    drunk_pirate.right(i)
    drunk_pirate.forward(step)

heading_of_pirate = drunk_pirate.heading()
print("Heading of pirate:", heading_of_pirate)

wn.mainloop()
