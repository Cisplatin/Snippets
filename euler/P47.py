"""
Distinct Primes Factors
Problem 47
"""

# To be honest, this approach kind of sucks. I dislike solutions where
# the program might have to change parameters to work (in this case,
# UPPER_BOUND). A smarter solution, in retrospect, would be to create
# a sieve-like algorithm where we increment each passed slot. Then
# we can go through the array and check for 4 factors (or better yet,
# check only when the increment results in a 4, so you only have to check
# neighbours).
#
# I would write it again but I'm lazy, and this one already works in less
# than 5 seconds.

# We use an arbitrary upper_bound, and throw an error if no case is found
LOWER_BOUND = 2
UPPER_BOUND = 1000000

# The number of distinct factors to have in each DISTINCT number
DISTINCT = 4

# We know that primes only have one prime factor, so we calculate these
# ahead of time to save some computing
def prime_sieves():
    erato, primes, exists = [True] * UPPER_BOUND, [], {}
    for i in xrange(2, UPPER_BOUND):
        if erato[i]:
            primes.append(i)
            exists[i] = True
            for j in xrange(i, UPPER_BOUND, i):
                erato[j] = False
    return (primes, exists)
primes, exists = prime_sieves()

# Continue going from LOWER_BOUND to UPPER_BOUND, checking for divisors
solved, count = 0, False
for n in xrange(LOWER_BOUND, UPPER_BOUND):
    # Find all prime factors by going through the primes we pre-calculated.
    # If we find a distinct one, we add to the count
    index, distinct, n_copy = 0, 0, n
    while n > 1 and n not in exists:
        if n % primes[index] == 0:
            distinct += 1
            while n % primes[index] == 0:
                n /= primes[index]
        index += 1

    # Should the loop end before n <= 1, then n is a prime, meaning we have
    # another prime factor, so we account for this
    if n > 1:
        distinct += 1

    # We update the count depending on if we have enough factors
    count = count + 1 if distinct == DISTINCT else 0

    # Should the count equal DISTINCT, we have solved the problem
    if count == DISTINCT:
        solved = True
        break

# We check if we actually have a solution; if not, upper bound is too small
if solved:
    print n_copy - DISTINCT + 1
else:
    raise Exception("UPPER_BOUND not high enough.")
