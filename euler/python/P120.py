"""
Square Remainders
Problem 120
"""

LOWER_LIMIT = 3
UPPER_LIMIT = 1000

# We go through each possible n from 0 to a. If n is even, the result is 2 (which can
# be found using the binomial theorem). Otherwise the result is 2na.
print sum(max(2 * a * n % (a * a) for n in xrange(a)) for a in xrange(LOWER_LIMIT, UPPER_LIMIT + 1))
