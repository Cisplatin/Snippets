"""
Cuboid Route
Problem 86
"""

# TODO Comment and explain code

from math import sqrt

SOLUTIONS = 1000000

if __name__ == '__main__':
    count = 0
    A = 1

    while count < SOLUTIONS:
        print count
        A += 1
        A_sqr = A ** 2
        for C in xrange(2, 2 * A + 1):
            length = sqrt(A_sqr + C ** 2)
            if length == int(length):
                if C > A:
                    count += (C - 2 * (C - A - 1)) / 2
                else:
                    count += C / 2
    print A
