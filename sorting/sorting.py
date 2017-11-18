"""
@fileoverview An implementation of various sorting algorithms.
@author Simon Hajjar <simon.j.hajjar@gmail.com>
"""

# Sorts the given array using the Bubble Sort algorithm, O(n^2).
# @param array [List] The array to sort.
# @effect Sorts the given array in-place.
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

# Sorts the given array using the Merge Sort algorithm, O(nlogn).
# @param array [List] The array to sort.
# @return [List] The sorted list.
def merge_sort(array):
    # Merges two sorted lists into one sorted list.
    # @param array_1 [List] The first sorted array.
    # @param array_2 [List] The second sorted array.
    # @return [List] The combined sorted array.
    def merge_lists(array_1, array_2):
        final_array = []
        while array_1 and array_2:
            i = array_1.pop(0) if array_1[0] < array_2[0] else array_2.pop(0)
            final_array.append(i)

        # After one list is empty, the rest of the other list can be appended.
        final_array.extend(array_1)
        final_array.extend(array_2)
        return final_array

    # Base case for the recursion.
    if len(array) < 2:
        return array

    # Otherwise, split the list in half and sort the halves.
    mid_point = len(array) / 2
    array_1 = merge_sort(array[:mid_point])
    array_2 = merge_sort(array[mid_point:])
    return merge_lists(array_1, array_2)

# Sorts the given array using the Counting Sort algorithm, O(n).
# @param array [List<Integer>] The array to sort.
# @return [List<Integer>] The sorted list.
def counting_sort(array):
    counts = [0 for i in xrange(max(array) + 1)]
    for element in array:
        counts[element] += 1
    array = []
    for i in xrange(len(counts)):
        array.extend([i] * counts[i])
    return array

from random import randint
from time import time

size = 5000
array = [randint(0, 10000) for i in xrange(size)]

start = time()
array = counting_sort(array)
end = time()

print end - start
print all(array[i] <= array[i + 1] for i in xrange(len(array) - 1))
