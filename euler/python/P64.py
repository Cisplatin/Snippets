"""
Odd Period Square Roots
Problem 64
"""

from math import sqrt

UPPER_LIMIT = 10000

def continued_fraction_period(n):
    # Given a number n, we find all the coefficients for the infinite continued fraction of
    # it's square root. We use the techniques found at:
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

    # First we check if it's a perfect square, in which case it will have a period of zero.
    root = int(sqrt(n))
    if root * root == n:
        return False

    # Run the algorithm for checking each co-efficient.
    m_n, d_n, a_n = 0, 1, root
    found_pairs = {}
    while (a_n, d_n, m_n) not in found_pairs:
        found_pairs[(a_n, d_n, m_n)] = True
        m_n = d_n * a_n - m_n
        d_n = (n - m_n * m_n) / d_n
        a_n = (root + m_n) / d_n

    # Return whether the period is odd or not.
    return (len(found_pairs) - 1) % 2

if __name__ == '__main__':
    # Check each number for how many continued fraction coefficients there are.
    print sum(map(continued_fraction_period, xrange(UPPER_LIMIT + 1)))
