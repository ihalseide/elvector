"""
elvector

Vector operations for iterables of real numbers.
Note:
    This module uses lists or tuples of real numbers to represent vectors.
    For the operation functions between two "vectors", the result will
    consider up to the length of the longest iterable and will fill missing
    ones in the shorter one with zeros.
"""

__author__ = "Izak Halseide"

import math
from itertools import zip_longest

def x(iter_a):
    """Get the 1st value of iter_a, which represents X."""
    return iter_a[0]

def y(iter_a):
    """Get the 2nd value of iter_a, which represents Y."""
    return iter_a[1]

def z(iter_a):
    """Get the 3rd value of iter_a, which represents Z."""
    return iter_a[2]

def add(iter_a, iter_b):
    """
    Return a new list with values of iter_a added to the values of iter_b
    elementwise.
    """
    return [a + b for a, b in zip_longest(iter_a, iter_b, fillvalue=0)]

def angle(iter_a):
    """Return the angle of the given vector in radians."""
    try: ax = x(iter_a)
    except IndexError:
        raise ValueError("empty vector")
    try: ay = y(iter_a)
    except IndexError:
        ay = 0
    return math.atan2(ay, ax)
    
def avg(iter_a):
    """Return the average value of a list."""
    return sum(iter_a) / len(iter_a)

def div(iter_a, scalar):
    """Return a new list with the values of iter_a divided by the scalar."""
    if scalar == 0:
        raise ZeroDivisionError("division by zero")
    return [a / scalar for a in iter_a]

def dot(iter_a, iter_b):
    """Returns the dot product of the arguments."""
    theta = angle(iter_a) - angle(iter_b)
    return mag(iter_a) * mag(iter_b) * math.cos(theta)

# can use an array of a zero because of zip_longest filling in for iter_a
def mid(iter_a, iter_b=[0]):
    """Return the list midpoint between a and b."""
    return [avg(ab) for ab in zip_longest(iter_a, iter_b, fillvalue=0)]

def mag(iter_a):
    """Return the Euclidean magnitude of a list of numbers."""
    return math.sqrt(sum(a**2 for a in iter_a))

def sub(iter_a, iter_b):
    """
    Return a new list with values of iter_a subtracted by the values of
    iter_b elementwise.
    """
    return [a - b for a, b in zip_longest(iter_a, iter_b, fillvalue=0)]

def dist(iter_a, iter_b):
    """Return the Euclidean distance between the two points."""
    return math.sqrt(sum((a - b)**2 for a, b in zip_longest(iter_a, iter_b,
                                                            fillvalue=0)))

def lerp(iter_a, iter_b, ratio):
    """
    Returns a Vector which is a linear interpolation between the first
    parameter and the second. The third parameter determines how far between
    the first parameter and the other that the result is going to be. It must
    be a value between 0 and 1 where 0 means the first parameter and 1 means
    the second will be returned.
    """
    return add(mult(iter_a, ratio), mult(iter_b, 1-ratio))

def norm(iter_a):
    """Return a normalized version of a list."""
    m = mag(iter_a)
    return div(iter_a, m)

def is_norm(iter_a):
    """Return True if the magnitude of iter_a is 1, False otherwise."""
    return mag(iter_a) == 1

def mult(iter_a, scalar):
    """Return a new list with the values of iter_a multiplied by the scalar."""
    return [a * scalar for a in iter_a]

def prod(iter_a):
    """Return the result of multiplying all the values in the iterable."""
    total = 1
    for a in iter_a:
        total *= a
        # short circuit: once it's zero there's no going back
        if total == 0:
            break
    return total

def scale_to(iter_a, scalar):
    """Scale a vector the a given length/magnitude."""
    n = norm(iter_a)
    return mult(n, scalar)

def to_polar(iter_a, full_mag=False):
    """
    Get polar representation of a vector (2D). "Full_mag" tells
    whether to include the magnitude from dimensions higher than the 2nd in
    the result.
    """
    if full_mag:
        m = mag(iter_a)
    else:
        m = mag(iter_a[:2])
    return m, angle(iter_a[:2])

def from_polar(r, theta):
    """
    Create a rectangular vector from polar representation. The parameters are
    radius/magnitude and then theta/angle (given in radians).
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y
