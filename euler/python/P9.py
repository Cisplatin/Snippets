"""
Special Pythagorean Triplet
Problem 9
"""

SUM = 1000

if __name__ == '__main__':
    # With some algebra we find a formula that must be satisfied for a and b
    # to be the sought after Pythagorean triplet. We brute force possibilities.
    products = []
    for a in range(1, SUM):
        for b in range(a, SUM):
            if 2 * (SUM * (a + b) - a * b) == SUM * SUM:
                products.append(a * b * (SUM - a - b))
    # In case there are multiple solutions, return the first found one
    print products[0]
