"""
Pandigital Products
Problem 32
"""

BASE = 10
MAXIMUM_MULTIPLIER = BASE ** 5

if __name__ == '__main__':
    # Because, if the smallest argument is as small as possible (which is 2),
    # the second argument can only be up to four digits long, as the total
    # lengths would than be more than possible otherwise.
    # We start from 2 because 1 * n = n would never be a pandigital.
    products, pandigital_sorted = set(), [str(i) for i in xrange(1, BASE)]
    for i in xrange(2, MAXIMUM_MULTIPLIER):
        j, current = i, ''

        # When we end up getting BASE digits or higher in our numbers, we
        # move on to the next value of i
        while len(current) < BASE:
            j += 1
            current = str(i) + str(j) + str(i * j)
            if sorted(current) == pandigital_sorted:
                products.add(i * j)

    # Print out the final sum
    print sum(products)
