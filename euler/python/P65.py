"""
Convergents of e
Problem 65
"""

from fractions import Fraction

FIRST_CONVERGENT = 2 # The first convergent of e.
CONVERGENTS = 100    # The number of convergents to compute.

# A generator for each partial value of e.
# @param count [Integer] The number of partial values to output for e.
# @return [Integer] The next partial value for e.
def generate_partial_values(count):
    outputs = 1
    current_multiple = 2
    while outputs < count:
        # Every third partial value is the next multiple of 2 (for e)
        if outputs % 3 == 2:
            yield current_multiple
            current_multiple += 2
        # Every other partial value is 1
        else:
            yield 1
        outputs += 1

if __name__ == '__main__':
    # Create the fraction bottom-to-top by reversing the partial value list
    fraction = Fraction(0)
    for value in reversed(list(generate_partial_values(CONVERGENTS))):
        fraction = Fraction(1, fraction + value)
    numerator = (fraction + FIRST_CONVERGENT).numerator

    # Find the sum of the numerator digits
    print sum(map(int, list(str(numerator))))
