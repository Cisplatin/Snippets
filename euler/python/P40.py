"""
Champernowne's Constant
Problem 40
"""

BASE = 10
MINIMUM, MAXIMUM = 0, 6

if __name__ == '__main__':
    # We first calculate the constant as a string. Because numbers have more
    # than one digits, we estimate that we only need to calculate up to 10^5
    constant = reduce(lambda x, y: x + str(y), xrange(BASE ** 5), '')

    # Returns the product of all numbers in the list n
    def product(n):
        return reduce(lambda x, y: x * y, n, 1)

    # We now find all digits that we need and multiply them
    print product(int(constant[BASE ** i]) for i in xrange(MINIMUM, MAXIMUM))
