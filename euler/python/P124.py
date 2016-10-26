"""
Sorted Radicals
Problem 124
"""

INDEX = 10000
UPPER_BOUND = 100001
LOWEST_PRIME = 2

if __name__ == '__main__':
    # We run a custom sieve whereby we set each element's radicals
    radicals = [1] * (UPPER_BOUND)
    for prime in xrange(LOWEST_PRIME, UPPER_BOUND):
        if radicals[prime] == 1:
            for composite in xrange(prime, UPPER_BOUND, prime):
                radicals[composite] *= prime

    # Sort the radicals and find the required element
    radical, number = sorted(zip(radicals, xrange(UPPER_BOUND)))[INDEX]
    print number
