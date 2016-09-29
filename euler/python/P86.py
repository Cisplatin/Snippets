"""
Cuboid Route
Problem 86
"""

from math import sqrt

DISTINCT_CUBOIDS = 1000000

if __name__ == '__main__':
    max_side, found_cuboids = 1, 0

    # Continue until the count of distinct cuboids is past the threshold.
    while found_cuboids < DISTINCT_CUBOIDS:

        # Assume we have an A x B x C cuboid, where A >= B >= C. A proof is
        # too hard to write without a markdown language, but on paper
        # it can be shown that the shortest length is sqrt(A^2 + (B + C)^2).
        # Thus we only have to check that the inside of the sqrt function is
        # a perfect square. Moreover, we only have to check values of (B + C)
        # from 2 to 2A, and just add the count by the number of times that
        # we can add to the number (B + C).
        max_side += 1

        # Note that we only have to check the range starting at 2, because
        # B and C are both positive integers so B + C >= 2, and we don't have
        # to consider when B + C = A, because then the length is A * sqrt(2),
        # which is never an integer for integer A.
        for min_side_sum in xrange(2, 2 * max_side):

            # Calculate the length and check if it's an integer. This is faster
            # than any techniques that directly check if our sum is a square
            length = sqrt(max_side ** 2 + min_side_sum ** 2)
            if length == int(length):

                # If the length is an integer, we add the number of ways that
                # the sides could add up to min_side_sum.
                if min_side_sum > max_side:
                    found_cuboids += (max_side + 1) - (min_side_sum + 1) / 2
                else:
                    found_cuboids += min_side_sum / 2

    # Print the maximal side length we tested to reach the threshold
    print max_side
