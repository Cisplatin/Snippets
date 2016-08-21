"""
Powerful Digit Sum
Problem 56
"""

from itertools import product

LIMIT = 100

if __name__ == '__main__':
    # We brute-force the solution and find the maximum
    nums = (str(a ** b) for a, b in product(range(1, LIMIT), repeat=2))
    print max(sum(int(j) for j in i) for i in nums)
