"""
Right Triangles with Integer Coordinates
Problem 91
"""

MAX_DIMENSION = 50

from itertools import product

if __name__ == '__main__':
    # We first add all triangles that have a point on either the y-axis or x-axis. For each
    # of these points, we know there are MAX_DIMENSION triangles that can be made.
    triangles = 2 * MAX_DIMENSION ** 2

    # Fix the origin and one other point, A. Connect these points with a line OA. Then we can find
    # a point B such that OAB is a right triangle by selecting a point on the line that intersects
    # A and is perpendicular to OA. We do this for each possible A that is not on the axes.
    # Note that no double-counting is made because A is the point with the right angle.
    for a in xrange(1, MAX_DIMENSION + 1):
        for b in xrange(a, MAX_DIMENSION + 1):

            # The line OA has a slope of A.y / A.x and has an intercept of 0. So the line can be
            # described as y = xA.y / A.x. The perpendicular line would then have a slope of
            # -A.x / A.y. We want to find the particular line that intersects A, so we have that
            # A.y = -A.x^2 / A.y + b, or that b = (A.y^2 + A.x^2) / (A.y). Thus the equation
            # (where we set A.x := a and A.y := b) is y = (b^2 + a^2 - xa) / b. So we just need
            # solutions (x, y) to this equation where x and y are integers in our bounds.
            max_y = a ** 2 + b ** 2
            limiter = max(0, max_y - a * MAX_DIMENSION)
            while max_y >= limiter:
                if max_y % b == 0 and max_y / b <= MAX_DIMENSION:
                    triangles += 1 + (a != b)
                max_y -= a

    # Print the final solution
    print triangles
