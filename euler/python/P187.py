"""
Semiprimes
Problem 187
"""

UPPER_LIMIT = 1000000
LOWEST_PRIME = 2

if __name__ == '__main__':
    # We generate prime numbers using the sieve of eratosthenes
    count, erato, primes = 0, [True] * UPPER_LIMIT, []

    # A function to find the index of the prime not exceeding the given value. Returns the index of
    # the element plus one. This is equivalent to the primes that can be multiplied.
    def prime_index(maximum, start, end):
        mid_point = (end + start) / 2
        if primes[end] <= maximum:
            return end + 1
        elif end - start <= 1:
            return start + 1
        elif primes[mid_point] > maximum:
            return prime_index(maximum, start, mid_point)
        else:
            return prime_index(maximum, mid_point, end)

    # We only need to check up to UPPER_LIMIT / 2 since we are multiplying the prime
    for prime in xrange(LOWEST_PRIME, UPPER_LIMIT / 2):
        if erato[prime]:
            primes.append(prime)
            count += prime_index(UPPER_LIMIT / prime, 0, len(primes) - 1)
            for composite in xrange(prime * prime, UPPER_LIMIT, prime):
                erato[composite] = False

    # Print out the final result
    print count
