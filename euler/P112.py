"""
Bouncy Numbers
Problem 112
"""

BASE = 10
PROPORTION = 0.99

if __name__ == '__main__':
    # We start from the numbers given to use in the problem, since 90% of
    # numbers below or equal to 21780 are bouncy.
    bouncy, current = 19602, 21780

    # To increase speed with the string converted bouncy numbers, we keep
    # a table of conversions for all digits
    digit_str = {str(i) : i for i in range(BASE)}

    # Because of the given starting point we do not need to check if current
    # is equal to zero
    while bouncy / float(current) != PROPORTION:
        current = current + 1

        # Keep track of whether the number is increasing or decreasing
        exist_l, exist_r = False, False

        # We calculate the last digit ahead of time since Python doesn't have
        # any do-while loops
        last_digit = current % BASE
        quotient = current / BASE

        # While no contradictions have been found, we continue
        while quotient > 0 and not (exist_l and exist_r):
            new_digit = quotient % BASE
            exist_l = exist_l or new_digit > last_digit
            exist_r = exist_r or new_digit < last_digit
            last_digit = new_digit
            quotient /= BASE

        # If we found a contradiction to increasing and decreasing, it's bouncy
        bouncy += exist_l and exist_r

    print current
