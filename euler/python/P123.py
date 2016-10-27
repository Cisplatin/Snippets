"""
Prime square remainders
Problem 123
"""

UPPER_LIMIT = 10 ** 10
PRIME_UPPER_BOUND = 300000
LOWEST_PRIME = 2

def find_remainder_exceeding(upper_limit):
    sieve = [True] * PRIME_UPPER_BOUND
    prime_count = 1
    for prime in xrange(LOWEST_PRIME, PRIME_UPPER_BOUND):
        if sieve[prime]:
            # We have found a new prime, and so we check if it fits the conditions
            prime_count += 1

            # We can simplify the original expression as follows
            if 2 * prime * (prime_count) % (prime * prime) > UPPER_LIMIT:
                return prime_count

            # If it's not the solution, just carry on with the sieve
            for composite in xrange(prime * prime, PRIME_UPPER_BOUND, prime):
                sieve[composite] = False

    # The sieve was not large enough to find the number
    raise Exception("UPPER_LIMIT was not high enough.")

print find_remainder_exceeding(UPPER_LIMIT)
