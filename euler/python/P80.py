"""
Square Root Digital Expansion
Problem 80
"""

from math import sqrt
from decimal import *

UPPER_LIMIT = 100
PRECISION = 100

if __name__ == '__main__':
    total_sum = 0

    # Pre-generate squares to save some time
    limit = int(sqrt(UPPER_LIMIT)) + 1
    squares = set(i * i for i in xrange(limit))

    # We need a bit more precision due to wonky getcontext() stuff
    getcontext().prec = PRECISION + limit
    for candidate in xrange(UPPER_LIMIT + 1):
        # Skip perfect squares
        if not candidate in squares:
            # Add the first 100 decimal digits
            total_sum += sum(map(int, str(Decimal(candidate).sqrt()).replace('.', '')[:PRECISION]))

    # Print the final answer
    print total_sum
