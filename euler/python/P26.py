"""
Reciprocal Cycles
Problem 26
"""

LOWER_LIMIT = 2
UPPER_LIMIT = 1000

# Finds the length of the repeating segment of 1 / n using long division
def repeating(n):
    # We keep track of the current remainder, and how many integers have been passed
    current, count, remainders = 1, 0, {}
    while not current in remainders:
        # Keep track of which integer we're at currently
        count += 1
        remainders[current] = count

        # If the remainder is now zero, there is no repeating part
        if current == 0:
            return 0

        # Otherwise, we find the next remainder
        while current < n:
            current *= 10
        current %= n
    return count - remainders[current] + 1

if __name__ == '__main__':
    # Find the maximum value of repeating(i) for each i from LOWER_LIMIT to UPPER_LIMIT
    max_value, max_denominator = 0, 0
    for i in xrange(LOWER_LIMIT, UPPER_LIMIT):
        repeat = repeating(i)
        if repeat > max_value:
            max_denominator, max_value = i, repeat
    print max_denominator
