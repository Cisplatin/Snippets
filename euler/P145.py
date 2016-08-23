"""
How many reversible numbers are there below one-billion?
Problem 145
"""

UPPER_BOUND = 1000000000

if __name__ == '__main__':
    def reversible(n):
        # After fixing the parity (as stated below), we check that the first
        # digit is greater than the last digit, to avoid doing double work.
        # Kind of sucks to have to use strings since they're so slow, but
        # so it goes.
        n_str = str(n)
        first_digit = int(n_str[0])
        n += first_digit % 2
        if first_digit > n % 10:
            return False

        # The question states that leading-zeros are not counted, so we check
        # if the reversed number would have any leading-zeros before reversing
        if n % 10 == 0:
            return False

        # String conversion, once again, is slow, so we use integer
        # arithmetic to determine the reverse of n
        reverse, n_temp = n % 10, n / 10
        while n_temp > 0:
            reverse *= 10
            reverse += n_temp % 10
            n_temp /= 10
        n += reverse

        # Finally, we check each digit of the sum of n and its reverse. If
        # we find even one number, we return false. If all are odd, we exit
        # the loop and return true.
        while n > 0:
            if n % 2 == 0:
                return False
            n /= 10
        return True

    # Although the question states that the UPPER_BOUND is a billion,
    # the program has shown that there are no numbers that satisfy this
    # property with nine digits. Not sure how to prove this, but it helps
    # to reduce the programming time.
    #
    # We also increment by two for the following reason - if a number's first
    # and last digit have the same parity then it cannot be reversible. Thus
    # we increment by two and fix the parity in the reversible() function. This
    # should cut time in half while still finding all the numbers.
    count = 0
    for i in xrange(1, UPPER_BOUND / 10, 2):
        # Because reversible returns true only if it is the lower of the two
        # numbers, we add two instead of one, to avoid the extra work.
        if reversible(i):
            count += 2
    print count
