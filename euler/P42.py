"""
Coded Triangle Numbers
Problem 42
"""

WORDS_TXT = "P42.txt"
HIGHEST_TRI_INDEX = 20

if __name__ == '__main__':
    # Calculate an arbitrary amount of triangle numbers
    triangle, exists = 0, {0 : True}
    for i in range(1, HIGHEST_TRI_INDEX):
        triangle += i
        exists[triangle] = True

    # Organize the file of words properly
    with open(WORDS_TXT, 'r') as f:
        words = [i[1:-1] for i in f.read().split(",")]

    # Convert each word into it's number, then check if it's a triangle number
    words = [sum(ord(j) - ord('@') for j in i) for i in words]
    print len(filter(lambda x: x in exists, words))
