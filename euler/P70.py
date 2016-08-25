"""
Totient Permutation
Problem 70
"""

from fractions import gcd

BASE = 10
LOWER_BOUND = 1
UPPER_BOUND = 10000000

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

# We prepare a function for determining if two numbers are permutations of
# each other quickly. To avoid string conversion, we use integer arithmetic.
def permutation(n, m):
    count = [0 for i in range(BASE)]
    while n > 0 and m > 0:
        count[n % BASE] += 1
        count[m % BASE] -= 1
        n /= BASE
        m /= BASE
    return m == 0 and n == 0 and all(count[i] == 0 for i in range(BASE))

# We then generate the rest of the numbers using the formula that, where
# d = gcd(m, n), t(mn) = t(n)t(m)d / t(d). If we generate the numbers one
# at a time, we just need to find one factor and we wil have the answer. We
# also check if each result is less than our current minimum. We start with
# our given that t(87109) = 79180
minimum_ratio = 87109 / float(79180)
minimum_value = 87109
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

# Go through each number and check if they have a new minimum
for n in range(LOWER_BOUND, UPPER_BOUND):
    # Generate the totient number of n. Unless we have already calculated it,
    # in which case it's prime and cannot be a permutation.
    if n in totient:
        continue
    find_totient(n)

    # Check the given number against the known minimum up to n. We check the
    # ratio before the permutation since the permutation is more expensive
    if float(n) / totient[n] < minimum_ratio and permutation(n, totient[n]):
            minimum_ratio, minimum_value = float(n) / totient[n], n

# Print the minimum value of n
print minimum_value
