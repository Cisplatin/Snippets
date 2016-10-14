"""
Pentagon Numbers
Problem 44
"""

from math import sqrt

# Calculates the nth pentagonal number
def pentagon(n, pentagons = {}):
    if not n in pentagons:
        pentagons[n] = n * (3 * n - 1) / 2
    return pentagons[n]

# Returns true if the given number is pentagonal, otherwise false
def is_pentagonal(n):
    n = (1 + sqrt(24 * n + 1)) / 6
    return n == int(n)

if __name__ == '__main__':
    # We check each pentagonal number until we find a solution
    found, current_pentagon = False, 1
    while not found:
        current_pentagon += 1
        p_i = pentagon(current_pentagon)

        # Check the current pentagonal number against every number below it
        for other_pentagon in xrange(1, current_pentagon):
            p_j = pentagon(other_pentagon)
            if is_pentagonal(p_i - p_j) and is_pentagonal(p_i + p_j):
                found = p_i - p_j

    # Print the final result
    print found
