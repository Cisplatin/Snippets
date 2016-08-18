"""
Summation of Primes
Problem 10
"""

CAP = 2000000
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
    # Return the sum of all primes below CAP, using the sieve of eratosthenes
    print sum(sieve(CAP))
