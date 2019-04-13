# Extend the above program so that the sides can be given to the function in any order.

def is_rightangled(a, b, c):
    a_list = [a, b, c]
    a_list.sort()  # It is necessary to sort because the hypotenuse is the bigger side
    x = a_list[2]**2
    y = a_list[0]**2 + a_list[1]**2
    return abs(x - y) < 0.000001

side1 = int(input("Type the length of side 1: "))
side2 = int(input("Type the length of side 2: "))
side3 = int(input("Type the length of side 3: "))

print("Is this a right-angle triangle? ", is_rightangled(side1, side2, side3))
