"""
Lychrel Numbers
Problem 55
"""

MAX_ITER = 50
UPPER_BOUND = 10000

if __name__ == '__main__':
    # We keep track of all the found required for each numbers. An element in
    # found has a value of None if it's Lychrel, and it's chain length else.
    found, count = {}, 0

    # Go through each number and check if it's a Lychrel number
    for i in range(UPPER_BOUND):
        # Go through each iteration
        passed = []
        for j in range(MAX_ITER):
            # Append the new possibility
            passed.append(str(i))

            # Check if the last number was already a found Lychrel. If so, we
            # only have information about the first value.
            if passed[-1] in found and found[passed[-1]] == None:
                found[k] = None
                count += 1
                break

            # Check if the last number was already a found number
            elif passed[-1] in found:
                for value, k in enumerate(range(len(passed) - 1)):
                    if len(passed) - k + found[passed[-1]] < MAX_ITER:
                        found[value] = len(passed) - k + found[passed[-1]]
                    else:
                        found[value] = None
                        count += 1
                break

            # Check if the last number is a palindrome
            elif len(passed) > 1 and passed[-1] == passed[-1][::-1]:
                for k in range(len(passed) - 1):
                    found[passed[k]] = len(passed) - k
                break

            # Check if it's the last iteration
            elif j == MAX_ITER - 1:
                found[passed[0]] = None
                count += 1
                break

            # All checks have passed so we find the iteration
            else:
                i += int(str(i)[::-1])

    # Print the count at the end
    print count
