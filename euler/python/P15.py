"""
Lattice Paths
Problem 15
"""

from math import factorial

DIM = 20

if __name__ == '__main__':
    # To go from the top left corner to the bottom right corner of a 20 x 20
    # grid, only moving left and down, you must move left exactly 20 times,
    # and down exactly 20 times. Thus there are 40 moves, 20 of which you must
    # choose to be downwards, and so the solution is 40 choose 20
    numerator = reduce(lambda x, y: x * y, range(DIM + 1, 2 * DIM + 1))
    print numerator / reduce(lambda x, y: x * y, range(1, DIM + 1))
