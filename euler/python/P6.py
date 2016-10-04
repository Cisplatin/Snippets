"""
Sum Square Difference
Problem 6
"""

CAP = 100

if __name__ == '__main__':
    # Find the sum of squares and the square of sums and find the difference
    print sum(xrange(CAP + 1)) ** 2 - sum(i ** 2 for i in xrange(CAP + 1))
