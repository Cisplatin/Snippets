"""
Goldbach's Other Conjecture
Problem 46
"""

from math import sqrt

# We try the problem to some arbitrary limit. If it's not high enough, we throw
# an exception. This is the highest composite number we check.
UPPER_BOUND = 10000
LOWEST_PRIME = 2
LOWEST_COMPOSITE = 3
CONJ_CONSTANT = 2

# We first gather a set of prime numbers to check against
erato, primes = [True] * UPPER_BOUND, {}
for i in xrange(LOWEST_PRIME, UPPER_BOUND):
    if erato[i]:
        primes[i] = True
        for j in xrange(i * i, UPPER_BOUND, i):
            erato[j] = False

# Next, we calculate all twice-squares until they become larger than UPPER_BOUND
t_square_range = xrange(int(sqrt(UPPER_BOUND / CONJ_CONSTANT)) + 1)
t_squares = [CONJ_CONSTANT * i * i for i in t_square_range]

# Finally, we check odd composite numbers until we find a counter-example
counter_example = None
for i in xrange(LOWEST_COMPOSITE, UPPER_BOUND, CONJ_CONSTANT):
    if not any(i - t in primes for t in t_squares):
        counter_example = i
        break

# If no solution was found, UPPER_BOUND was not high enough
if counter_example == None:
    raise Exception("UPPER_BOUND not high enough.")

# Otherwise, print out the solution
print counter_example
