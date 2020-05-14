# elvector
Python vector operations on iterables (a silly little idea I had one day).

# functions
`x(iter_a)`:
    Get the 1st value of iter_a, which represents X.

`y(iter_a)`:
    Get the 2nd value of iter_a, which represents Y.

`z(iter_a)`:
    Get the 3rd value of iter_a, which represents Z.

`add(iter_a, iter_b)`:
    Return a new list with values of iter_a added to the values of iter_b
    elementwise.

`angle(iter_a)`:
    Return the angle of the given vector in radians.
    
`avg(iter_a)`:
    Return the average value of a list.

`div(iter_a, scalar)`:
    Return a new list with the values of iter_a divided by the scalar.

`dot(iter_a, iter_b)`:
    Returns the dot product of the arguments.

`mid(iter_a, iter_b=[0])`:
    Return the list midpoint between a and b.

`mag(iter_a)`:
    Return the Euclidean magnitude of a list of numbers.

`sub(iter_a, iter_b)`:
    Return a new list with values of iter_a subtracted by the values of
    iter_b elementwise.

`dist(iter_a, iter_b)`:
    Return the Euclidean distance between the two points.

`lerp(iter_a, iter_b, ratio)`:
    Returns a Vector which is a linear interpolation between the first
    parameter and the second. The third parameter determines how far between
    the first parameter and the other that the result is going to be. It must
    be a value between 0 and 1 where 0 means the first parameter and 1 means
    the second will be returned.

`norm(iter_a)`:
    Return a normalized version of a list.

`is_norm(iter_a)`:
    Return True if the magnitude of iter_a is 1, False otherwise.

`mult(iter_a, scalar)`:
    Return a new list with the values of iter_a multiplied by the scalar.

`prod(iter_a)`:
    Return the result of multiplying all the values in the iterable.

`scale_to(iter_a, scalar)`:
    Scale a vector the a given length/magnitude.

`to_polar(iter_a, full_mag=False)`:
    Get polar representation of a vector (2D). "Full_mag" tells
    whether to include the magnitude from dimensions higher than the 2nd in
    the result.

`from_polar(r, theta)`:
    Create a rectangular vector from polar representation. The parameters are
    radius/magnitude and then theta/angle (given in radians).
    
Archived 2020-05-14.
