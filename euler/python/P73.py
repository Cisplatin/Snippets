"""
Counting Fractions in a Range
Prblem 73
"""

UPPER_LIMIT = 12000
LOWEST_PRIME = 2
OTHER_FRACTION = (1, 3)

from fractions import gcd

# Let t(n) be Euler's totient function. We know that for all primes p,
# t(p) = p - 1. Thus, when we generate the primes, we assign their
# dictionary value to be p - 1
def primes():
    erato, primes = [True] * UPPER_LIMIT, {}
    for i in xrange(2, UPPER_LIMIT):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes[i] = i - 1
            for j in xrange(i, UPPER_LIMIT, i):
                erato[j] = False
    return primes
totient = primes()

# We also know that t(1) = 1, so we add that
totient[1] = 1

# We then generate the rest of the numbers using the formula that, where
# d = gcd(m, n), t(mn) = t(n)t(m)d / t(d). If we generate the numbers one
# at a time, we just need to find one factor and we wil have the answer. We
# also check if each result is greater than our current maximum
def find_totient(k):
    # Check to find just one factor, and then we can apply the formula. We will
    # have to find at least one since LOWER_BOUND = 2 for this problem
    factor = LOWEST_PRIME
    while k % factor != 0:
        factor += 1

    # Apply the formula with the found factor and add it to our dictionary.
    # Note that n = factor, m = k / factor, and d = gcd(factor, k / factor). We
    # store the numbers so we don't have to calculate them more than once.
    n, m = factor, k / factor
    d = gcd(n, m)
    totient[k] = totient[n] * totient[m] * d / totient[d]
    return totient[k]

if __name__ == '__main__':
    # Find the size of F_n. This is done by using |F_n| = |F_(n-1)| + phi(n)
    farey_sequence_size = sum(find_totient(i) for i in xrange(LOWEST_PRIME, UPPER_LIMIT + 1))

    # The position of 1/2 will be the sequence size divided by 2, via:
    # https://en.wikipedia.org/wiki/Farey_sequence
    index_difference = (farey_sequence_size + 1) / 2 - 2

    # We now generate all numbers in the sequence until we find 1/3
    farey_1, farey_2 = (0, 1), (1, UPPER_LIMIT)
    while farey_2 != OTHER_FRACTION:
        index_difference -= 1

        # Generate the next number using the Farey sequence algorithm
        common_term = int((UPPER_LIMIT + farey_1[1]) / farey_2[1])
        new_farey = (common_term * farey_2[0] - farey_1[0], common_term * farey_2[1] - farey_1[1])
        farey_1, farey_2 = farey_2, new_farey

    # Print the final answer
    print index_difference
