"""
Roman Numerals
Problem 89
"""

from collections import OrderedDict

# We store each possible value of roman numeral
ROMAN = OrderedDict([
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
])
ROMAN_TXT = "P89.txt"

# Returns the digits saved by writing the minimal form of n
def minimal_roman(n):
    numerical, skip_next, minimal = 0, False, ""

    # First we find the numerical value
    for i in xrange(len(n)):
        if skip_next:
            skip_next = False
        elif n[i:i + 2] in ROMAN:
            numerical += ROMAN[n[i:i + 2]]
            skip_next = True
        else:
            numerical += ROMAN[n[i]]

    # We then find the roman value
    for numeral in ROMAN:
        entries = int(numerical / ROMAN[numeral])
        minimal += numeral * entries
        numerical -= ROMAN[numeral] * entries

    # Now we return the length difference
    return len(n) - len(minimal)

if __name__ == '__main__':
    # Convert each number to an integer, find the real representation, and find the length
    # difference
    print sum(map(lambda x: minimal_roman(x.replace('\n', '')), open(ROMAN_TXT, 'r').readlines()))
