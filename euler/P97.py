"""
Large Non-Mersenne Prime
Problem 97
"""

BASE = 10
DIGITS = 10
COEFFICIENT = 28433
POWER = 7830457

if __name__ == '__main__':
    # We calculate the number but only maintain the last DIGITS digits, leaving
    # us with the final number.
    modulos, num = BASE ** DIGITS, COEFFICIENT
    for i in xrange(POWER):
        num = (num * 2) % modulos
    print num + 1
