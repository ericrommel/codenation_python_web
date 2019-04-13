# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the
# triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return
# True if the triangle is right-angled, or False otherwise.
#
# Hint: Floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for
# equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up
# as:
# if  abs(x-y) < 0.000001:    # If x is approximately equal to y

def is_rightangled(a, b, c):
    if c > a and c > b:
        x = c**2
        y = b**2 + a**2
    else:
        return "False. The side 3 should be the longest onde."
    return abs(x - y) < 0.000001

side1 = int(input("Type the length of side 1: "))
side2 = int(input("Type the length of side 2: "))
side3 = int(input("Type the length of side 3: "))

print("Is this a right-angle triangle? ", is_rightangled(side1, side2, side3))
