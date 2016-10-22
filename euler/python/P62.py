"""
Cubic Permutations
Problem 62
"""

POWER = 3
PERMUTATIONS = 5
BASE = 10

if __name__ == '__main__':
    # We go through each cube until we find one with three permutations
    current, permutations = 1, {0 : []}

    # We keep track of the number of permutations for current, as well as the current maximum
    # so that we can update the number of digits
    current_key, current_max = 0, BASE
    while len(permutations[current_key]) != PERMUTATIONS:
        # Increment our current and find the cube
        current += 1
        cube = current ** POWER
        sorted_cube = str(sorted(str(cube)))

        # If we get more digits we can reset the permutations
        if cube > current_max:
            permutations = {}
            current_max *= BASE

        # Check if we already found a permutation
        current_key = -1
        for other_permutation in permutations:
            if sorted_cube == other_permutation:
                current_key = other_permutation
                permutations[current_key].append(current)
                break

        # If we didn't find a permutation, add a new one
        if current_key == -1:
            current_key = str(sorted(str(cube)))
            permutations[current_key] = [current]

    # Print the cube of the minimum number we found. Since we add them in order, the first
    # element will be the minimum.
    print permutations[current_key][0] ** POWER
