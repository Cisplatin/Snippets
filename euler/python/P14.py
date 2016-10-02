"""
Longest Collatz Sequence
Problem 14
"""

MAX_START = 1000000

if __name__ == '__main__':
    # Keep all known chain lengths in a hash
    chain_lengths = {0 : 0, 1 : 1}

    # A recursive function to find and update collatz chains
    def collatz(i):
        if not i in chain_lengths:
            next_item = i / 2 if i % 2 == 0 else 3 * i + 1
            chain_lengths[i] = collatz(next_item) + 1
        return chain_lengths[i]

    # Find the values for all numbers up to MAX_START
    print max((collatz(i), i) for i in xrange(MAX_START))[1]
