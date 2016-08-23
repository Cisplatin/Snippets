"""
Efficient Exponentiation
Problem 122
"""

from itertools import product
from collections import defaultdict

# The range for possible values of k, not including 1 since we know that.
MAXIMUM_K = 25
K_RANGE = xrange(2, MAXIMUM_K + 1)

# We store all known multiplications for each number.
minimums = []
possible = {i : [] for i in K_RANGE}
possible[1] = [set()]

# Calculate the minimum by double-checking if we re-use exponents
def calc_min(n, m):
    # At most the minimum is n + m, so we set is as such
    minimum = n + m

    # Go through each possibility for summing found
    for i, j in product(possible[n], possible[m]):
        # Create a new possibility that uses two previous possibilities
        union = i.union(j)
        union.update({n, m})
        minimum, good_set = min(len(union), minimum), True

        # Check if a subset of this already exists
        for other_set in possible[n + m]:
            if union >= other_set:
                found_set = False
                break
            elif other_set > union:
                possible[n + m].remove(other_set)
        if good_set:
            possible[n + m].append(union)
    return minimum

if __name__ == '__main__':
    # We go through each possible value of k.
    minimums = []
    for k in K_RANGE:
        minimums.append(min(calc_min(i, k - i) for i in range(1, k / 2 + 1)))
    print sum(minimums)
