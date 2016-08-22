"""
Number Spiral Diagonals
Problem 28
"""

from itertools import product

DIM = 1001

if __name__ == '__main__':
    # We use a general formula found through inspection
    print sum(i * (i - j) + j for i, j in product(range(3, DIM + 1, 2), range(4))) + 1
