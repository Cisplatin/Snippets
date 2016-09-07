"""
Sub-string Divisibility
Problem 43
"""

DIV = [2, 3, 5, 7, 11, 13, 17]
BASE = 10

# Returns all permutations of the given array
def permutate(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        for j in permutate(arr[:i] + arr[i + 1:]):
            result += [[arr[i]] + j]
    return result

# We find all permutations of 0-9 (inclusively), which will allow us to
# generate the pandigital numbers. We generate these numbers here, and then
# filter out all for which the first digit is zero
pandigital = map(lambda x: ''.join(map(str, x)), permutate(range(BASE)))
pandigital = filter(lambda x: x[0] != '0', pandigital)

# Next, we check for each divisibilty as required by the question
divisible = (lambda x: all(int(x[i + 1:i + 4]) % DIV[i] == 0 for i in range(len(DIV))))

# Print the final sum of pandigitals
print sum(map(int, filter(divisible, pandigital)))
