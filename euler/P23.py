"""
Non-abundant Sums
Problem 23
"""

from math import sqrt

MAX = 28124

if __name__ == '__main__':
    # We calculate the sum of divisors a bit faster by finding pairs of
    # divisors, and only going up to sqrt(n)
    abundant = []
    for i in range(MAX):
        divisors = range(2, int(sqrt(i)) + 1)
        if sum(i / j + j * (j != i / j) for j in divisors if not i % j) > i:
            abundant.append(i)

    # Now that we have all abundant numbers, we filter out any integers that
    # are not the sum of two abundant numbers by finding all sums and comparing
    exists = {i + j : True for i in abundant for j in abundant}
    print sum(filter(lambda x: x not in exists, range(MAX)))
