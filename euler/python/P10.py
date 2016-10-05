"""
Summation of Primes
Problem 10
"""

UPPER_LIMIT = 2000000
LOWEST_PRIME = 2

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to UPPER_LIMIT
    erato = [True] * UPPER_LIMIT
    for prime in xrange(LOWEST_PRIME, UPPER_LIMIT):
        if erato[prime]:
            # We found a prime, so switch off all multiples
            yield prime
            for j in range(prime * prime, UPPER_LIMIT, prime):
                erato[j] = False

if __name__ == '__main__':
    # Return the sum of all primes below CAP, using the sieve of eratosthenes
    print sum(sieve())
