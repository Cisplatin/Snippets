"""
Smallest Multiple
Problem 5
"""

from math import log

MIN, MAX = 1, 20
LOWEST_PRIME = 2

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to cap
    erato = [True] * MAX
    for prime in xrange(LOWEST_PRIME, MAX):
        if erato[prime]:
            yield prime
            for composite in xrange(prime * prime, MAX, prime):
                erato[composite] = False

if __name__ == '__main__':
    # All prime numbers up to MAX
    primes, result = sieve(), 1

    # Find the maximum power of each prime number for each factor, and multiply
    # it by the result so far
    for i, prime in enumerate(primes):
        counts = (log(factor, prime) for factor in range(MIN, MAX + 1))
        result *= prime ** max(filter(lambda x: x.is_integer(), counts))
    print int(result)
