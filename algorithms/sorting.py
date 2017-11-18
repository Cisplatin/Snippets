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

# Searches the given sorted array using the Binary Search algorithm, O(logn).
# @param array [List<T>] The sorted list.
# @param value [T] The value to search for.
# @return [Integer] The index of the given value in the array, or -1 if the
#                   value was not in the array.
def binary_search(array, value):
    # Base case for the recursion.
    if len(array) == 0:
        return -1

    # If the mid-point is the value, we are done
    mid_point = len(array) / 2
    if array[mid_point] == value:
        return mid_point

    # If the mid-point is smaller, check the right half of the array. To assure
    # the correct index is returned, we also add the values of the array that
    # will be unknown in the next function call.
    elif array[mid_point] < value:
        index = binary_search(array[mid_point + 1:], value)
        if index >= 0:
            index += mid_point + 1
        return index

    # Otherwise, we check the left half of the array.
    else:
        return binary_search(array[:mid_point], value)
