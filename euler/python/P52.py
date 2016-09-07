"""
Permuted Multiples
Problem 52
"""

BOUND = 7

if __name__ == '__main__':
    # This program uses a brute-force solution, with the one optimization that
    # it stops early if one of the multiples don't match thanks to all()
    x = 1
    while not all(set(str(x * i)) == set(str(x)) for i in range(2, BOUND)):
        x += 1
    print x
