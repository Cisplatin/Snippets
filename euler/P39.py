"""
Integer Right Triangles
Problem 39
"""

from math import sqrt

MAX_P = 1000

if __name__ == '__main__':
    # We store all squares in both a dictionary (to check for existence),
    # and an array (to iterate through all possibilities)
    p_value, squares_iter, squares_dict = [0] * MAX_P, [], {}
    for i in xrange(MAX_P / 2):
        squares_iter.append(i * i)
        squares_dict[i * i] = i

    # We look for all triples within our checked array, and store the
    # maximal value found so far
    maximal_p = 0
    for i in xrange(len(squares_iter)):
        for j in xrange(i, len(squares_iter)):
            # If the hypotenuse squared is not found, we continue
            c = squares_iter[i] + squares_iter[j]
            if c not in squares_dict:
                continue

            # If it is found and our permimeter is not out of reach,
            # then we add to the value and check if it exceeds our maximal
            p = i + j + squares_dict[c]
            if p < MAX_P:
                p_value[p] += 1
                if p_value[p] > p_value[maximal_p]:
                    maximal_p = p

    # Print out the final result
    print maximal_p
