"""
Digit Factorials
Problem 34
"""

from math import factorial

BASE = 10
UPPER_BOUND = 10000000

if __name__ == '__main__':
    # For faster calculations we store the fifth facts ahead of time
    fact = {str(i) : factorial(i) for i in range(BASE)}
    sum_of_fact = (lambda x: sum(fact[i] for i in str(x)) == x)

    # We know that 8 * 9^5 is less than 10,000,000, so the biggest number
    # can't be more than a million. Thus we use that as our upper bound.
    print sum(filter(sum_of_fact, range(3, UPPER_BOUND)))
