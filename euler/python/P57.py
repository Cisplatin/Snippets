"""
Square Root Convergents
Problem 57
"""

ITERATIONS = 1000

class Fraction:
    # Creates a new fraction
    def __init__(self, num, den):
        self.num, self.den = num, den

    # Set the fraction to be the next iteration, and return True if the digits
    # in the numerator exceed the digits in the denominator
    def next_iteration(self):
        self.num += self.den                    # Add one to the fraction
        self.num, self.den = self.den, self.num # Invert the fraction
        self.num += self.den                    # Add one to the fraction
        return len(str(self.num)) > len(str(self.den))

if __name__ == '__main__':
    fraction = Fraction(3, 2)
    print sum(fraction.next_iteration() for i in xrange(ITERATIONS))
