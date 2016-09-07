"""
Combinatoric Selections
Problem 53
"""

N_MIN, N_MAX = 1, 100
THRESHOLD = 1000000

if __name__ == '__main__':
    # Store all the found combinations in a dictionary.
    known, total = {}, 0

    # Go through each value of n to calculate.
    for n in xrange(N_MIN, N_MAX + 1):
        # Note that nC0 is always equal to 1, as well as nCn
        known[(n, 0)] = known[(n, n)] = 1

        # Note that nCr is equal to nC(n-r), so we only calculate one and set
        # both to be equal to it
        for r in xrange(1, n / 2 + 1):
            known[(n, r)] = known[(n - 1, r - 1)] + known[(n - 1, r)]
            known[(n, n - r)] = known[(n, r)]

            # If the solution is above the threshold, we add, but make sure to
            # not double-count
            if known[(n, r)] > THRESHOLD:
                total += 1 + (n - r != r)

    # Print the final count
    print total
