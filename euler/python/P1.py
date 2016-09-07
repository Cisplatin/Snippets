"""
Multiples of 3 and 5
Problem 1
"""

MAX = 1000
MULTIPLE = [3, 5]

if __name__ == '__main__':
    # Generates all numbers from 0 to MAX that are a multiple
    # of any number in MULTIPLE
    print sum(i for i in range(MAX) if not all(i % j for j in MULTIPLE))
