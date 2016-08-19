"""
Lexicographic Permutations
Problem 24
"""

UPPER_BOUND = 10
PERMUTATION = 1000000

if __name__ == '__main__':
    # We try the brute force approach of finding every permutation, ordering
    # them, and then finding the millionth one
    numbers = range(UPPER_BOUND)

    # Returns all permutations of the given array
    def permutate(arr):
        if len(arr) <= 1:
            return [arr]
        result = []
        for i in range(len(arr)):
            for j in permutate(arr[:i] + arr[i + 1:]):
                result += [[arr[i]] + j]
        return result

    # Print the correct permutation
    result = permutate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[PERMUTATION - 1]
    print ''.join(str(i) for i in result)
