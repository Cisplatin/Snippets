"""
Pandigital Fibonacci Ends
Problem 104
"""

BASE = 10
F_0, F_1 = 0, 1

# A generator for all fibonacci numbers
def fibonacci():
    f_n, f_m = F_0, F_1
    while True:
        f_n, f_m = f_m, f_n + f_m
        yield f_n

# A function that returns true if the first 10 digits and last 10 digits are
# pandigital numbers
def pandigital(n):
    # If the number is not at least 10 digits long, it cannot be pandigital
    n = str(n)
    if len(n) < BASE - 1:
        return False

    # The number does not have the property if and only if a count of some
    # digit rises to 2. Thus, we check against everytime we add a count.
    counts = {'0' : True}
    for i in xrange(BASE - 1):
        if n[-(i + 1)] in counts or n[i] in counts:
            return False
        counts[n[i]] = True
        counts[n[-(i + 1)]] = True
    return True

# Generate each fibonacci number and check if it has the given property
k, current = 1, fibonacci()
while not pandigital(current.next()):
    k += 1
    print k
print k
