"""
Digit Fifth Powers
Problem 30
"""

BASE = 10
POWER = 5
UPPER_BOUND = 1000000

if __name__ == '__main__':
    # For faster calculations we store the fifth powers ahead of time
    power = {str(i) : i ** POWER for i in range(BASE)}
    sum_of_fifth = (lambda x: sum(power[i] for i in str(x)) == x)

    # We know that 7 * 9^5 is less than 1,000,000, so the biggest number
    # can't be more than a million. Thus we use that as our upper bound.
    print sum(filter(sum_of_fifth, range(2, UPPER_BOUND)))
