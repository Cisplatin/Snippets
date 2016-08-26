"""
Spiral Primes
Problem 58
"""

from math import sqrt

THRESHOLD = 0.1
DIAGONALS = 4

if __name__ == '__main__':
    # We start from the center and slowly extend outwards until UPPER_BOUND
    current, square, prime_count, ratio = 1, 1, 0, 1

    # Create a function to test for primality
    def is_prime(n):
        if n == 2:
            return True
        # We do a simple "check for factors up to sqrt(n)"
        for i in xrange(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    while ratio > THRESHOLD:

        # We increment along the bottom-right digonal as squares are the
        # easiest of the diagonals to follow
        current += 2
        square = current * current

        # A square will never be prime so we don't need to worry about the
        # bottom-right. We just check the other three possibilities
        for i in xrange(1, DIAGONALS):
            if is_prime(square - (i * (current - 1))):
                prime_count += 1

        # Update the new ratio
        ratio = prime_count / float(current * 2 - 1)

    print current
