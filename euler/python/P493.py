"""
Under the Rainbow
Problem 493
"""

from itertools import product

COLORS = 7
NUMBER_OF_EACH = 10
PICKED_BALLS = 20
DIGITS_REQUIRED = 9

# Returns the product of all items in the list n
def mult(n):
    return reduce(lambda x, y: x * y, n, 1)

# Returns the value of n choose r
def choose(n, r, known = {}):
    if (n, r) not in known:
        known[(n, r)] = mult(range(n - r + 1, n + 1)) / mult(range(1, r + 1))
    return known[(n, r)]

# Returns the probability of getting x distinct colors
def distinct_colors(x):
    total = 0.0
    for balls in product(range(1, NUMBER_OF_EACH + 1), repeat=x):
        if sum(balls) == PICKED_BALLS:
            total += mult(choose(NUMBER_OF_EACH, i) for i in balls)
    total *= choose(COLORS, x)
    return total / choose(COLORS * NUMBER_OF_EACH, PICKED_BALLS)

if __name__ == '__main__':
    # Get the expected value of the probability function, round it to the right
    # number of digits, and print it
    expected = sum(i * distinct_colors(i) for i in xrange(1, COLORS + 1))
    print repr(round(expected, DIGITS_REQUIRED))
