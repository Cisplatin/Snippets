"""
Sum of a Square and a Cube
Problem 348
"""

# This is a very slow solution - about O(NlogN). A faster solution would be
# to generate palindromes first, and then check if the difference of each
# palindrome and each cube is a square or not, leading to O(N^5/6)

from collections import defaultdict
from itertools import product

SUM_COUNT = 4
PALINDROMES = 5
UPPER_BOUND = 50000

# We pre-calculate squares and cubes for an arbitrary limit
squares = (i ** 2 for i in xrange(UPPER_BOUND))
cubes = (i ** 3 for i in xrange(UPPER_BOUND))

# We check each possibility and add all palindromes to a list
counts, solutions = defaultdict(int), []
for i, j in product(squares, cubes):
    # Calculate the sum and check if it's a palindrome
    ij_sum = i + j
    ij_sum_str = str(ij_sum)
    if ij_sum_str == ij_sum_str[::-1]:
        counts[ij_sum] += 1

        # If we hit four, we append it to our solutions. If we go above it,
        # remove it from the solutions
        if counts[ij_sum] == SUM_COUNT:
            solutions.append(ij_sum)
            if len(solutions) == PALINDROMES:
                break

# We print out the final solution
if len(solutions) < PALINDROMES:
    raise Exception("UPPER_BOUND not high enough.")
print sum(sorted(solutions)[:PALINDROMES])
