"""
Digit Factorial Chains
Problem 74
"""

from math import factorial
from collections import OrderedDict

BASE = 10
UPPER_BOUND = 1000000
CHAIN_LENGTH = 60

if __name__ == '__main__':
    # We pre-calculate factorials to save some time
    fact = {str(i) : factorial(i) for i in range(BASE)}

    # Store known chain lengths (i.e. chain[69] = 5), and the number so far
    chain, count = {}, 0

    # Go through every number and check chain lengths
    for current in range(UPPER_BOUND):
        # Store the numbers we found in this chain to check for repeating. We
        # use an ordered dictionary so that we can iterate through them after
        # as well.
        passed = OrderedDict()

        # Keep calculating the sum of factorials until we find a repeat. We
        # track the index for faster chain calculation later.
        index = 0
        while not current in chain and not current in passed:
            passed[current] = index
            index += 1
            current = sum(fact[i] for i in str(current))

        # Now that the chain is done, we update the chain lengths for each
        # passed element. For all elements in the cycle, the length is the same
        # We only do this if the last element was not found in chain.
        if not current in chain:
            length = len(passed) - index
            for i in range(length):
                chain[passed.popitem()[0]] = length
            # If the length is CHAIN_LENGTH we add all the elements
            if length == CHAIN_LENGTH:
                count += length
        else:
            length = chain[current]

        # Then we update those elements not in the chain. For these, we add
        # one to the length each time. We also check for the CHAIN_LENGTH.
        while passed:
            length += 1
            if length == CHAIN_LENGTH:
                count += 1
            chain[passed.popitem()[0]] = length

    # We print the final count
    print count
