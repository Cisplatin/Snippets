"""
Circular Primes
Problem 35
"""

UPPER_BOUND = 1000000
EVEN_DIGITS = ['0', '2', '4', '6', '8']

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to UPPER_BOUND
    erato, primes = [True] * UPPER_BOUND, {'2' : True}
    for i in xrange(2, UPPER_BOUND):
        if erato[i]:
            # We found a prime, so switch off all multiples. The prime is only
            # valid if it does not contain even digits.
            if not any(j in str(i) for j in EVEN_DIGITS):
                primes[str(i)] = True
            for j in xrange(i, UPPER_BOUND, i):
                erato[j] = False
    return primes

if __name__ == '__main__':
    # We go through each prime below a million and check each rotation
    primes = sieve()
    print sum(all(p[i:] + p[:i] in primes for i in range(len(p))) for p in primes)
