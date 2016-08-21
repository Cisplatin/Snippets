"""
Circular Primes
Problem 35
"""

UPPER_BOUND = 1000000
LOWEST_PRIME = 2

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to UPPER_BOUND
    erato, primes = [True] * UPPER_BOUND, {}
    for i in range(LOWEST_PRIME, UPPER_BOUND):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes[i] = True
            for j in range(i, UPPER_BOUND, i):
                erato[j] = False
    return primes

if __name__ == '__main__':
    # We check each prime that we have sieved
    primes, count = sieve(), 0
    for prime in primes:
        circular = True
        for i in range(len(str(prime))):
            rotation = int(str(prime)[1:] + str(prime)[0])
            if rotation not in primes:
                circular = False
                break
        if circular:
            count += 1
    print count
