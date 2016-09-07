"""
Quadratic Primes
Problem 27
"""

from itertools import product

UPPER_BOUND = 100000
AB_LIMIT = 1000
LOWEST_PRIME = 2

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to UPPER_BOUND
    erato, primes = [True] * UPPER_BOUND, {}
    for i in range(LOWEST_PRIME, UPPER_BOUND):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes[i], primes[-i] = True, True
            for j in range(i, UPPER_BOUND, i):
                erato[j] = False
    return primes

if __name__ == '__main__':
    # Returns the number of primes given the coefficients. There is an
    # arbitrary limit on the sieve, given that the number won't get too big
    primes = sieve()
    def chain_length(a, b, n=1):
        # Assume the first output is prime given that it is b
        while abs(n * (n + a) + b) in primes:
            n += 1
        return n

    # Try out all possible combonations and check if there are primes. We only
    # need to check prime b's because n=0 is equal to b
    max_chain, max_a, max_b, limits = 0, 0, 0, range(-AB_LIMIT, AB_LIMIT + 1)
    for a, b in product(limits, filter(lambda x: x <= AB_LIMIT, primes)):
        new_length = chain_length(a, b)
        if new_length > max_chain:
            max_chain, max_a, max_b = new_length, a, b
    print max_a * max_b
