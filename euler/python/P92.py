"""
Square Digit Chains
Problem 92
"""

from math import log

BASE = 10
UPPER_BOUND = 10000000
END_INTEGER = 89

if __name__ == '__main__':
    # We pre-calculate squares to save some time
    squares = {str(i) : i ** 2 for i in range(BASE)}

    # Store known chain ends (i.e. chain[85] = 89), and the number of chains
    # so far that end at 89
    end, count = {1 : 1, END_INTEGER : END_INTEGER}, 1

    # Go through every number up to 7 * 9^2 (as this is the maximum value of
    # the sum of squares of digits up to 10^7) and find the result
    maximum = int(log(UPPER_BOUND, BASE)) * (BASE - 1) ** 2 + 1
    for current in xrange(1, maximum):
        # Store the numbers we found in this chain to update them afterwards
        passed = []

        # Keep calculating the sum of squares until we find END_INTEGER or 1
        while not current in end:
            passed.append(current)
            current = sum(squares[i] for i in str(current))

        # If current is END_INTEGER, we update the count
        if end[current] == END_INTEGER:
            count += len(passed)

        # Now that the chain is done, we update all elements in passed
        while passed:
            end[passed.pop()] = end[current]

    # For the rest of the numbers, we simply add to the count if the number's
    # sum of squares is END_INTEGER
    for current in xrange(maximum, UPPER_BOUND):
        if end[sum(squares[i] for i in str(current))] == END_INTEGER:
            count += 1

    # We print the final count
    print count
