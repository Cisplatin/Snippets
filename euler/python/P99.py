"""
Largest Exponential
Problem 99
"""

BASE_EXP_TXT = "P99.txt"

from math import log

if __name__ == '__main__':
    # First we make the file read-able
    with open(BASE_EXP_TXT, 'r') as f:
        powers = map(lambda x: map(int, x.strip().split(",")), f.readlines())

    # Then we find the maximum using log identities. Namely, that log(a^x) = alog(x). We then add
    # one because we are currenty 0-indexed instead of 1-indexed.
    BASE, POWER = 0, 1
    print max((line[POWER] * log(line[BASE]), index) for index, line in enumerate(powers))[1] + 1
