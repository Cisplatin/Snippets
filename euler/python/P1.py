"""
Multiples of 3 and 5
Problem 1
"""

MAX = 1000
MULTIPLES = [3, 5]

if __name__ == '__main__':
    # Generates all numbers from 0 to MAX that are a multiple of any number
    # within MULTIPLE
    print sum(i for i in xrange(MAX) if not all(i % j for j in MULTIPLES))
