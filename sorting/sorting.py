"""
@fileoverview An implementation of various sorting algorithms.
@author Simon Hajjar <simon.j.hajjar@gmail.com>
"""

# Sorts the given array using the Bubble Sort algorithm, O(n^2).
# @param array [List] The array to sort.
# @effect Sorts the given array.
# @return [List] The sorted list.
def bubble_sort(array):
    # Note that, after an iteration, every element after the last swap
    # is sorted. Thus, we don't need to check those elements.
    last_swap = len(array) - 1
    for iteration in xrange(len(array)):
        swap = False
        for i in xrange(last_swap):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
                last_swap = i + 1

        # If we go through an iteration and nothing is swapped, then we can
        # skip the rest of the iterations.
        if not swap:
            return array
    return array

from random import randint
from time import time

size = 5000
array = [randint(0, 10000) for i in xrange(size)]

start = time()
bubble_sort(array)
end = time()

print end - start
print all(array[i] <= array[i + 1] for i in xrange(len(array) - 1))
