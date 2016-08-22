"""
Double-Base Palindrome
Problem 36
"""

BOUND = 1000000

if __name__ == '__main__':
    # First we find all base-10 palindromes
    palindromes = filter(lambda x: x == x[::-1], map(str, range(BOUND)))

    # We now filter out those palindromes that are not binary
    binary = (lambda x: "{0:b}".format(x) == "{0:b}".format(x)[::-1])
    print sum(filter(binary, map(int, palindromes)))
