"""
Sum Square Difference
Problem 6
"""

CAP = 100

if __name__ == '__main__':
    # Find the sum of squares and the square of sums and find the difference
    print sum(range(CAP + 1)) ** 2 - sum(i * i for i in range(CAP + 1))
