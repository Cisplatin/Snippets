"""
Names Scores
Problem 22
"""

NAMES_TXT = "P22.txt"

if __name__ == '__main__':
    # First, open the text file and sort the contents
    with open(NAMES_TXT, 'r') as names_file:
        names = sorted([i[1:-1] for i in names_file.read().split(",")])

    # Calculate the score of each name and sum
    score = (lambda (x, y): (x + 1) * sum([ord(i) - ord('A') + 1 for i in y]))
    print sum(map(score, enumerate(names)))
