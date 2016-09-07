"""
Smallest Multiple
Problem 5
"""

from math import log

MIN = 1
MAX = 20
LOWEST_PRIME = 2

def sieve(cap):
    # Runs the sieve of eratosthenes to find prime numbers up to cap
    erato, primes = [True] * cap, []
    for i in range(LOWEST_PRIME, cap):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes.append(i)
            for j in range(i, cap, i):
                erato[j] = False
    return primes

if __name__ == '__main__':
    # All prime numbers up to MAX
    primes, result = sieve(MAX), 1

    # Find the maximum power of each prime number for each factor, and multiply
    # it by the result so far
    for i, prime in enumerate(primes):
        counts = (log(factor, prime) for factor in range(MIN, MAX + 1))
        result *= prime ** max(filter(lambda x: x.is_integer(), counts))
    print int(result)
