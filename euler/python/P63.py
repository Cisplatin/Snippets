"""
Powerful Digit Counts
Problem 63
"""

BASE = 10

# We continually multiply by the given number until the power exceeds the
# number of digits. At this point, because the base will always be below 10,
# the number of digits will be unable to catch-up. We subtract one as to
# not include the case where the power is zero.
def base_powers(n):
    power, product = 1, n
    while len(str(product)) == power:
        power, product = power + 1, product * n
    return power - 1

# We know that the base of the power cannot be more than 9, as if this is the
# case the number will not be the correct amount of digits.
print sum(base_powers(i) for i in xrange(1, BASE))
