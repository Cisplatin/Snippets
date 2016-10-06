"""
Passcode Derivation
Problem 79
"""

from collections import defaultdict

KEYLOG_TXT = "P79.txt"
BASE = 10

# The following algorithm only works if there is strictly one possible key
# that can be formed consistently
if __name__ == '__main__':

    # Get all the derivations and make them read-able
    with open(KEYLOG_TXT, 'r') as f:
        keys = [i[:-1] for i in f.readlines()]

    # Get all digits that must come after each digit
    after = defaultdict(set)
    for key in keys:
        for digit in xrange(len(key)):
            for after_digit in xrange(digit + 1, len(key)):
                after[key[digit]].add(key[after_digit])
        if key[digit] not in after:
            after[key[digit]] = set()

    # Find each first digit after making sure it's not after any other digit
    passcode, digits_left = '', after.keys()
    while digits_left:
        for key in digits_left:
            if not any(key in after[i] for i in digits_left):
                digits_left.remove(key)
                passcode += key
                for other_key in after:
                    if key in after[other_key]:
                        after[other_key].remove(key)

    # Print the final result
    print passcode
