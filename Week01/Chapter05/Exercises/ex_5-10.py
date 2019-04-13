# Write a function find_hypot which, given the length of two sides of a right-angled triangle, returns the length of
# the hypotenuse. (Hint: x ** 0.5 will return the square root.)

# Formula: c**2 = a**2 + b**2

def find_hypot(a, b):
    sum = a**2 + b**2
    c = sum**0.5
    return c

side1 = int(input("Type the length of side 1: "))
side2 = int(input("Type the length of side 2: "))

print("The length of hypotenuse is ", int(find_hypot(side1, side2)))
