"""
Trunctable Primes
Problem 37
"""

NUMBER_OF_SOLUTIONS = 11
UPPER_BOUND = 1000000
BAD_DIGITS = ['0', '4', '6', '8']
NOT_TRUNC = ['2', '3', '5', '7']

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to UPPER_BOUND
    erato, primes = [True] * UPPER_BOUND, {}
    for i in xrange(2, UPPER_BOUND):
        if erato[i]:
            # We found a prime, so switch off all multiples. We only return
            # it if it doesn't contain any digits and is not of length one
            if not any(j in str(i) for j in BAD_DIGITS):
                primes[str(i)] = True
            for j in xrange(i, UPPER_BOUND, i):
                erato[j] = False
    return primes

if __name__ == '__main__':
    # We go through each prime below a million and check each trunctability
    primes = sieve()
    trunc_prime = (lambda x: all(x[i:] in primes and x[:-i] in primes \
        for i in range(1, len(x))))
    result = filter(lambda x: x not in NOT_TRUNC, filter(trunc_prime, primes))
    if len(result) < NUMBER_OF_SOLUTIONS:
        raise Exception("UPPER_BOUND not high enough.")
    print sum(map(int, result))
