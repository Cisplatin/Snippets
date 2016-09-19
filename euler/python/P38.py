"""
Pandigital Products
Problem 38
"""

BASE = 10

# Returns the product if the given number can create a pandigital product. Else
# returns zero.
def pandigital_product(n):
    found, k, result = {'0' : True}, 1, ""
    while len(result) < BASE - 1:
        for i in str(k * n):
            if i in found:
                return
            found[i] = True
        result, k = result + str(k * n), k + 1
    return result * (len(result) == BASE - 1)

# Find the largest pandigital product of all possible numbers. Note that the
# maximum it can be is BASE ** (BASE / 2) as any higher and the number would
# not be able to work even for n = 2
print max(pandigital_product(i) for i in xrange(BASE ** (BASE / 2)))
