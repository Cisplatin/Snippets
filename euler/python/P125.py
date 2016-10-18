"""
Palindromic Sums
Problem 125
"""

from math import sqrt

UPPER_LIMIT = 10 ** 8

if __name__ == '__main__':
    # We only need to check up to sqrt(UPPER_LIMIT) since we square each number
    maximum = int(sqrt(UPPER_LIMIT))

    # Since there may be duplicates, we store all results in a hash and sum afterwards
    final_sum = {}

    # Go through each possible starting number
    for i in xrange(1, maximum):
        # We start the cons_sum at the starting number and the increment of it, as we need at
        # least two numbers to have a consecutive sum of squares. Thus the next number to add
        # would be i + 2
        cons_sum = i ** 2 + (i + 1) ** 2
        next_int = i + 2

        # Make sure the sum has not exceeded the limit
        while cons_sum < UPPER_LIMIT:
            # We store as a string to save conversion time
            palindrome = str(cons_sum)
            if palindrome == palindrome[::-1]:
                final_sum[cons_sum] = True
            cons_sum += next_int ** 2
            next_int += 1

    # Print all numbers that appeared
    print sum(final_sum.keys())
