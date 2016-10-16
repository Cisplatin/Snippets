"""
Square on the Inside
Problem 504
"""

from math import sqrt
from itertools import product

UPPER_LIMIT = 100

if __name__ == '__main__':
    # We first calculate the number of lattice points under every line that starts on the positive
    # y-axis and ends at the positive x-axis, with integer intercepts below the upper limit.
    lattice = {}

    # We only check for lines where y >= x, and then add that and the rotation to our lattice
    for x in xrange(1, UPPER_LIMIT + 1):
        for y in xrange(x, UPPER_LIMIT + 1):
            # Find the sum of points under the line but above the origin
            points = sum(int(y - y * point / float(x)) for point in xrange(1, x))

            # Remove any points that lie on the line
            points -= sum(y * point % x == 0 for point in xrange(1, x))

            # Add both points to the lattice
            lattice[(x, y)] = lattice[(y, x)] = points

    # Go through each possible quadrilateral and find the number of lattice points. We set our
    # ranges to minimize checking rotations
    total_count = 0
    for a, b in product(xrange(1, UPPER_LIMIT + 1), repeat=2):
        for c, d in product(xrange(a, UPPER_LIMIT + 1), xrange(b, UPPER_LIMIT + 1)):

            # First we add all the points on the axes, including the origin
            points = a + b + c + d - 3

            # Then we add all points within the quadrants
            points += sum(lattice[point] for point in [(a, b), (b, c), (c, d), (d, a)])

            # We now check if the final number of points is a perfect square
            if sqrt(points) == int(sqrt(points)):
                # We add the correct amount of rotations depending on what is possible
                total_count += 1 if (a == c and b == d) else 2 if (a == c or b == d) else 4

    # Print the final result
    print total_count
