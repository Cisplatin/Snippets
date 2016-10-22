"""
Digit Cancelling Fractions
Problem 33
"""

from fractions import gcd

MINIMUM = 10
MAXIMUM = 100

if __name__ == '__main__':
    # We multiply the proper numerators/denominators and simplify at the end
    p_num, p_den = 1, 1

    # We iterate through each possible numerator and denominator
    for num in xrange(MINIMUM, MAXIMUM):
        for den in xrange(num + 1, MAXIMUM):
            # We find the adjusted numerator and denominator. First we check if there is a common
            # digit in both
            common = set(str(num)) & set(str(den))
            if len(common) != 1:
                continue
            common = common.pop()
            if common == '0':
                continue

            # Find the adjusted numerators and denominators
            a_num = ''.join(i for i in str(num) if i != common)
            a_den = ''.join(i for i in str(den) if i != common)

            # Make sure we got a non-empty cancellation
            if a_num == '' or a_den == '':
                continue
            a_num, a_den = int(a_num), int(a_den)

            # Find the gcd so that we can simplify
            n_gcd, a_gcd = gcd(num, den), gcd(a_num, a_den)
            n_num, n_den = num / n_gcd, den / n_gcd
            a_num, a_den = a_num / a_gcd, a_den / a_gcd

            # Check if the fractions are equivalent
            if a_num == n_num and a_den == n_den:
                p_num *= a_num
                p_den *= a_den

    # Print the final denominator
    print p_den / gcd(p_num, p_den)
