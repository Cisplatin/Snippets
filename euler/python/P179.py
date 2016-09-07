"""
Consecutive Positive Divisors
Problem 179
"""

LOWER_BOUND = 2
UPPER_BOUND = 10000000

# We save some time by finding all primes, as we know that each of them has
# only one divisor (itself). We also use these to calculate divisors
def prime_sieves():
    erato, primes, exists = [True] * UPPER_BOUND, [], {}
    for i in xrange(2, UPPER_BOUND):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes.append(i)
            exists[i] = True
            for j in xrange(i, UPPER_BOUND, i):
                erato[j] = False
    return (primes, exists)
primes, exists = prime_sieves()

# We now go through each number and count the divisors. If it's the same as
# the last number, then we add to the count.
prev_divisors, count = 0, 0
for n in xrange(LOWER_BOUND, UPPER_BOUND):
    # Find the number of divisors by using the fact that the number of divisors
    # is equal to the product of all prime multiples plus one
    index, divisors = 0, 1
    while n > 1 and n not in exists:
        if n % primes[index] == 0:
            # If it divides, we find out how many times by continually dividing
            exponent = 1
            while n % primes[index] == 0:
                n /= primes[index]
                exponent += 1
            divisors *= exponent
        index += 1

    # If the number is not equal to one by now, then it's a prime, so we
    # account for that in the divisors count
    if n > 1:
        divisors *= 2

    # If the divisors match up, add to the count
    if divisors == prev_divisors:
        count += 1
    prev_divisors = divisors

# Print out the final count
print count
