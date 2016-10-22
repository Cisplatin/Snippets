"""
Cubic Permutations
Problem 62
"""

PERMUTATIONS = 5

if __name__ == '__main__':
    # We go through each cube until we find one with three permutations
    current, permutations = 1, {0 : []}

    # We keep track of the number of permutations for current, as well as the current maximum
    # so that we can update the number of digits
    found_permutations, current_max = 0, 10
    while len(permutations[found_permutations]) != PERMUTATIONS:
        # Increment our current and find the cube
        current += 1
        cube = current ** 3
        sorted_cube = str(sorted(str(cube)))

        # If we get more digits we can reset the permutations
        if cube > current_max:
            permutations = {}
            current_max *= 10

        # Check if we already found a permutation
        found_permutations = -1
        for other_permutation in permutations:
            if sorted_cube == other_permutation:
                permutations[other_permutation].append(current)
                found_permutations = other_permutation
                break

        # If we didn't find a permutation, add a new one
        if found_permutations == -1:
            found_permutations = str(sorted(str(cube)))
            permutations[found_permutations] = [current]

    # Print the cube of the minimum number we found
    print min([found_permutations] + permutations[found_permutations]) ** 3
