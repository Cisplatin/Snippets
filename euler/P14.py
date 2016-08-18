"""
Longest Collatz Sequence
Problem 14
"""

MAX = 1000000

if __name__ == '__main__':
    # Keep all known chain lengths in a hash
    chain_lengths = {1 : 1}

    # A recursive function to find and update collatz chains
    def collatz(i):
        if not i in chain_lengths:
            if i % 2 == 0:
                result = collatz(i / 2)
            else:
                result = collatz(3 * i + 1)
            chain_lengths[i] = result + 1
        return chain_lengths[i]

    # Find the values for all numbers up to MAX
    max_chain_length, max_chain_number = 0, 0
    for num in range(1, MAX):
        length = collatz(num)
        if length > max_chain_length:
            max_chain_length, max_chain_number = length, num
    print max_chain_number

