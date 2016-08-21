"""
Permuted Multiples
Problem 52
"""

from sys import maxint

MULT_BOUND = 7

if __name__ == '__main__':
    # This program uses a brute-force solution, with the one optimization that
    # it stops early if one of the multiples don't match thanks to all()
    for x in xrange(1, maxint):
        if all(set(str(x * i)) == set(str(x)) for i in range(2, MULT_BOUND)):
            print x
            break
