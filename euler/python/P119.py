"""
Digit Power Sum
Problem 119
"""

INDEX = 30
UPPER_LIMIT = 75

if __name__ == '__main__':
    power_sums = []

    # We use an arbitrary upper limit, and find all powers of that limit to check for summation
    for n in xrange(UPPER_LIMIT):
        current = n
        while len(str(current)) < n:
            current *= n

            # If the sum of the digits is equal to n, we found a new power
            if sum(map(int, str(current))) == n:
                power_sums += [current]

    # Print the INDEX'th one and pray that the UPPER_LIMIT was high enough
    print sorted(power_sums)[INDEX - 1]
