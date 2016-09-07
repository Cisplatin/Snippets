"""
Power Digit Sum
Problem 16
"""

POWER = 1000

if __name__ == '__main__':
    # I love Python so much. We just calculate 2^1000 and sum the digits.
    print sum([int(i) for i in str(2 ** POWER)])
