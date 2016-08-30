"""
Pandigital Prime
Problem 41
"""

# This solution uses a modified Sieve of Eratosthenes, where instead of
# collecting all primes, we check for pandigitality, and if it holds, we
# store the prime as the largest prime pandigital.
#
# Note that we do not have to check for 9-pandigital numbers, since they
# cannot be prime. This is because the sum of their digits, which is 45,
# is divisible by 9, meaning that the number would also be divisible by 9.
# This brings our upper bound down to 10 ** 8 from 10 ** 9. The same logic
# can be applied to 8-pandigital numbers, bringing the limit down once more
# to 10 ** 7.

BASE, LOWEST_PRIME, LOWEST_CONSIDERED = 10, 2, 1
SIEVE_UPPER_BOUND = BASE ** 7

# Returns true if the given number is n-pandigital
def pandigital(n):
    n = str(n)
    count = {str(i) : 0 for i in xrange(LOWEST_CONSIDERED, len(n) + 1)}
    for i in n:
        if not i in count or count[i] == 1:
            return False
        count[i] += 1
    return True

# We start a sieve of eratosthenes.
erato, maximal_pandigital = [True] * SIEVE_UPPER_BOUND, 1
for i in xrange(LOWEST_PRIME, SIEVE_UPPER_BOUND):
    if erato[i]:
        for j in xrange(i * i, SIEVE_UPPER_BOUND, i):
            erato[j] = False

        # If this cell has been marked as a prime, assume such and check for
        # a pandigital number. If the number is n-pandigital, we replace our
        # old maximum, since numbers are traversed in order.
        if pandigital(i):
            maximal_pandigital = i

# Print the final solution.
print maximal_pandigital
