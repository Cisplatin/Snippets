"""
Distinct Powers
Problem 29
"""

from itertools import product

MIN, MAX = 2, 100

if __name__ == '__main__':
    # There aren't that many numbers so we just generate them all in a set
    print len(set(a ** b for a, b in product(range(MIN, MAX + 1), repeat=2)))
