"""
Totient Maximum
Problem 69
"""

from fractions import gcd

BASE = 10
LOWER_BOUND = 1
UPPER_BOUND = 1000000

# Let t(n) be Euler's totient function. We know that for all primes p,
# t(p) = p - 1. Thus, when we generate the primes, we assign their
# dictionary value to be p - 1
def primes():
    erato, primes = [True] * UPPER_BOUND, {}
    for i in xrange(2, UPPER_BOUND):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes[i] = i - 1
            for j in xrange(i, UPPER_BOUND, i):
                erato[j] = False
    return primes
totient = primes()

# We also know that t(1) = 1, so we add that
totient[1] = 1

# We then generate the rest of the numbers using the formula that, where
# d = gcd(m, n), t(mn) = t(n)t(m)d / t(d). If we generate the numbers one
# at a time, we just need to find one factor and we wil have the answer. We
# also check if each result is greater than our current maximum
maximum_ratio = maximum_value = 0
def find_totient(k):
    # Check to find just one factor, and then we can apply the formula. We will
    # have to find at least one since LOWER_BOUND = 2 for this problem
    factor = 2
    while k % factor != 0:
        factor += 1

    # Apply the formula with the found factor and add it to our dictionary.
    # Note that n = factor, m = k / factor, and d = gcd(factor, k / factor). We
    # store the numbers so we don't have to calculate them more than once.
    n, m = factor, k / factor
    d = gcd(n, m)
    totient[k] = totient[n] * totient[m] * d / totient[d]

# Go through each number and check if they have a new maximum
for n in range(LOWER_BOUND, UPPER_BOUND):
    # Generate the totient number of n. Unless we have already calculated it,
    # in which case it's prime and cannot be a permutation.
    if not n in totient:
        find_totient(n)

    # Check the given number against the known maximum up to n
    if float(n) / totient[n] > maximum_ratio:
        maximum_ratio, maximum_value = float(n) / totient[n], n

# Print the minimum value of n
print maximum_value
