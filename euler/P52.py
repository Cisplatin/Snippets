"""
Permuted Multiples
Problem 52
"""

MULT_BOUND = 7

if __name__ == '__main__':
    # This program uses a brute-force solution, with the one optimization that
    # it stops early if one of the multiples don't match thanks to all()
    found, x = False, 1
    while not found:
        if all(set(str(x * i)) == set(str(x)) for i in range(2, MULT_BOUND)):
            found = True
            print x
        else:
            x += 1
