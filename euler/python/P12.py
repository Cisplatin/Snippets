"""
Highly Divisible Triangular Numbers
Problem 12
"""

LOWEST_PRIME = 2
DIVISORS = 500
CAP = 100000

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to cap
    erato, primes = [True] * CAP, []
    for i in range(LOWEST_PRIME, CAP):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes.append(i)
            for j in range(i, CAP, i):
                erato[j] = False
    return primes

if __name__ == '__main__':
    # Run a sieve up to some arbitrary number and see if it solves
    primes, triangle, increment, divisors = sieve(), 0, 1, 1
    # Go through each triangle number and find the number of divisors
    while divisors < DIVISORS:
        # Increment to the next triangle number and rest divisors
        triangle, increment, divisors = triangle + increment, increment + 1, 1
        # Copy the triangle number over so that we may edit it
        buffer_tri = triangle
        for prime in primes:
            # Find the number of times this prime divides the buffer
            count = 1
            while buffer_tri % prime == 0:
                buffer_tri, count = buffer_tri / prime, count + 1
            # The number (x ^ a)(y ^ b) has (a + 1)(b + 1) divisors (where x
            # and y are prime numbers)
            divisors *= count
            # If we have reached 1, we no longer need to divide
            if buffer_tri == 1:
                break

        # If the buffer_tri has not hit one, then we haven't generated primes
        # If this occurs, simply increase the CAP constant
        if buffer_tri != 1:
            raise Exception("Not enough primes generated.")
    print triangle
