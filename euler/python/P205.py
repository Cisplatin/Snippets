"""
Dice Game
Problem 205
"""

from itertools import product
from collections import defaultdict

SOLUTION_DIGITS = 7
PETER, COLIN = 0, 1
SIDES, DICE = [4, 6], [9, 6]

if __name__ == '__main__':
    # First we get all possible rolls that can occur
    rolls = [defaultdict(int) for i in xrange(len(SIDES))]
    for i in xrange(len(SIDES)):
        for j in product(xrange(1, SIDES[i] + 1), repeat=DICE[i]):
            rolls[i][sum(j)] += 1

    # Count all the rolls that are greater for Peter
    count = sum(rolls[PETER][roll[PETER]] * rolls[COLIN][roll[COLIN]] \
                for roll in product(rolls[PETER], rolls[COLIN]) \
                if roll[PETER] > roll[COLIN])

    # Calculate the total possibilities
    total = sum(rolls[PETER][i] for i in rolls[PETER]) * \
            sum(rolls[COLIN][i] for i in rolls[COLIN])

    # Print the final fraction of wins
    print round(count / float(total), SOLUTION_DIGITS)
