"""
Triangular, Pentagonal, and Hexagonal
Problem 45
"""

LIMIT = 100000

if __name__ == '__main__':
    # We generate a bunch of each type of number and find the intersection,
    # and then find the second number in the list. We then arbitrary increase
    # the limit until we find the answer.

    # Note that all hexagonal numbers are also triangular numbers, so we do
    # not have to check triangle numbers
    pentagon = set((i * (3 * i - 1) / 2 for i in range(1, LIMIT)))
    hexagon = set((i * (2 * i - 1) for i in range(1, LIMIT)))
    try:
        print sorted(list(pentagon & hexagon))[2]
    except IndexError:
        print "LIMIT not set high enough."
