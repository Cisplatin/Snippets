"""
XOR Decryption
Problem 59
"""

from itertools import product

CIPHER_TXT = "P59.txt"
KEY_LENGTH = 3

if __name__ == '__main__':
    # We first make the file read-able
    with open(CIPHER_TXT, 'r') as f:
        cipher = map(int, f.read().replace('\n', '').split(','))

    # We check each possible key and look for spaces, as they're most common
    # in the English language
    final_plain, final_score = 0, 0
    for i, j, k in product(range(ord('a'), ord('z') + 1), repeat=KEY_LENGTH):

        # First we find the plain text associated with this key
        key = [i, j, k]
        plain = ''.join(chr(cipher[i] ^ key[i % 3]) for i in range(len(cipher)))

        # We now find a score for the plain text based on common words
        score = plain.count(' ')
        if score > final_score:
            final_plain, final_score = plain, score

    # Print the sum of the ASCII values for the final plain text
    print sum(ord(i) for i in final_plain)
