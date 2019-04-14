# We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function.
# Construct a small Python example to test whether this is possible, and write up your findings.

# Tuplas cannot be used as parameters in a function.
# def a_method(a, (b, c)):
#     (a, b) = (b, a)
#     return (a, b)

# BUT, we can use '*' to pass a tuple as a parameter since the number of tuple's elements match with number
# of function's elements
def a_method(a, b):
    (a, b) = (b, a)
    return (a, b)

def another_method(x, y):
    return x + y


(x, y, z) = input("Type any two values separeted by only one space: ").split(" ")


print(a_method(*(x, y)))

param = (x, y)

print(another_method(*a_method(*param)))
