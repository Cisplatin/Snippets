"""
Ordered Fractions
Problem 71
"""

UPPER_LIMIT = 1000000
FRACTION_NUM, FRACTION_DEN = 3.0, 7.0

# Returns true if the first fraction is greater than the second fraction
def fraction_greater(num_1, den_1, num_2, den_2):
    return num_1 * den_2 > num_2 * den_1

if __name__ == '__main__':
    num, den = 0, 1
    for denominator in xrange(1, UPPER_LIMIT):
        # The closest the number can get is where the numerator is multiplied by the
        # fraction in question.
        true_numer = int(denominator * FRACTION_NUM / FRACTION_DEN)
        if fraction_greater(true_numer, denominator, num, den) and \
           fraction_greater(FRACTION_NUM, FRACTION_DEN, true_numer, denominator):
           num, den = true_numer, denominator

    # Print final numerator
    print num
