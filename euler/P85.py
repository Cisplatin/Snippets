"""
Counting Rectangles
Problem 85
"""

from itertools import product

AREA = 2000000

# For a given m x n rectangle, we can fit an a x b rectangle (where
# 0 < a < m and 0 < b < n) a total of (m - a + 1)(n - b + 1) times.
# For a given m x n rectangle, we can find the total number of rectangles
# that fit by summing over the possible values of a and b.
def number_of_rectangles(m, n):
    total = 0
    for a, b in product(xrange(1, m + 1), xrange(1, n + 1)):
        total += (m - a + 1) * (n - b + 1)
    return total

# The number_of_rectangles function returns a value that is approximately
# (mn)^4, so we don't expect m or n to be larger than 100. Moreover, an m x n
# and n x m rectangle have the same solution, so we don't bother checking twice
upper_bound = 100
close_val, close_area = 0, 0
for m in xrange(1, upper_bound):
    for n in xrange(m, upper_bound):
        new_area = number_of_rectangles(m, n)
        if abs(new_area - AREA) < abs(close_val - AREA):
            close_area, close_val = m * n, new_area

print close_area
