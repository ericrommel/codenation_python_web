import math
import sys

def area(radius):
    b = 3.14159 * radius**2
    return b

def area2(radius):
    return 3.14159 * radius * radius

def area3(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

def area4(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def absolute_value2(x):
    if x < 0:
        return -x
    return x

def bad_absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return ""

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

def distance2(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def is_divisible(x, y):
    """ Test if x is exactly divisible by y """
    if x % y == 0:
        return True
    else:
        return False

def is_divisible2(x, y):
    return x % y == 0

def absolute_value_buggy_version(n):   # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        return 1
    elif n > 0:
        return n

# Tests #

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)
    test(absolute_value_buggy_version(17) == 17)
    test(absolute_value_buggy_version(-17) == 17)
    test(absolute_value_buggy_version(0) == 0)
    test(absolute_value_buggy_version(3.14) == 3.14)
    test(absolute_value_buggy_version(-3.14) == 3.14)

test_suite()        # Here is the call to run the tests
