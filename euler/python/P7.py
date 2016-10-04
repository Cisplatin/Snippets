"""
10001st Prime
Problem 7
"""

from math import log

PRIME = 10001
LOWEST_PRIME = 2

def sieve(cap):
    # Runs the sieve of eratosthenes to find prime numbers up to cap. Stops
    # when it finds the PRIME'th prime number
    erato, count = [True] * cap, 0
    for i in range(LOWEST_PRIME, cap):
        if erato[i]:
            # We found a prime, so switch off all multiples
            for j in range(i, cap, i):
                erato[j] = False
            count += 1
            if count == PRIME:
                return i

if __name__ == '__main__':
    # Calls on an adjusted sieve to find the correct prime.
    # There's a theorem with an upper bound for the nth prime number (n > 6).
    # We can use this result to predict what cap is required to find the
    # PRIME'th prime number.
    print sieve(int(PRIME * log(PRIME) + PRIME * log(log(PRIME) - 1)) + 1)
