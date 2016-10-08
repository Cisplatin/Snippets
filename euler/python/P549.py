"""
Divisibility of Factorials
Problem 549
"""

LOWER_LIMIT = 2
UPPER_LIMIT = 100

smallest = [0] * (UPPER_LIMIT + 1)
for prime in xrange(LOWER_LIMIT, UPPER_LIMIT + 1):
    # If the value is still zero, that means that the number is prime, so we
    # iterate with it and all of its powers.
    if smallest[prime] == 0:

        # Get each power of the prime and iterate through the list, updating
        # the value to whatever number is required to get that power.
        current_power, current_value = 1, prime

        # Keep tracks of the copies of the prime found so far in the factorial.
        primes_found, minimum = 1, prime

        # Go through the whole sieve
        while current_value <= UPPER_LIMIT:

            # Before sieving, we make sure that the current power we have can
            # divide our minimum factorial.
            while current_power > primes_found:

                # If it can't, we keep adding prime to the minimum factorial
                # until we have enough factors.
                minimum += prime

                # Check how many new prime factors the number has. Note that
                # we don't need to check the ones between minimum
                # and minimum + prime since there cannot be any.
                new_factor = minimum
                while new_factor % prime == 0:
                    primes_found += 1
                    new_factor /= prime

            # Go through each multiple of the power and make sure the number
            # is at least equal to our minimum
            for j in xrange(current_value, UPPER_LIMIT + 1, current_value):
                smallest[j] = max(smallest[j], minimum)

            # Go to the next prime power
            current_power += 1
            current_value *= prime

# Finally, sum all of the values
print sum(smallest)
