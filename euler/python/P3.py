"""
Largest Prime Factor
Problem 3
"""

from math import sqrt

NUM = 600851475143
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
    # Get all prime factors of the NUM, then print the largest
    print max((i for i in sieve(int(sqrt(NUM))) if NUM % i == 0))
