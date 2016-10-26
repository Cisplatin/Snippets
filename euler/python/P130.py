"""
Composites with Prime Repunit Property
Problem 130
"""

VALUES = 25
UPPER_LIMIT = 100000
LOWEST_PRIME = 2

if __name__ == '__main__':
    # First we generate composite numbers using a modified sieve of eratosthenes
    erato, composites = [True] * UPPER_LIMIT, []
    for prime in xrange(LOWEST_PRIME, UPPER_LIMIT):
        if erato[prime]:
            for composite in xrange(prime * prime, UPPER_LIMIT, prime):
                erato[composite] = False
        else:
            # Check that the composite has gcd(10, prime) = 1
            if prime % 2 != 0 and prime % 5 != 0:
                composites.append(prime)

    # Returns the minimal number that divides the repunit of length n
    def minimum_repunit(n):
        repunit = 1
        while repunit % n != 0:
            repunit *= 10
            repunit += 1
        return len(str(repunit))

    # Go through each composite and check if n - 1 is divisible by A(n)
    solutions = []
    current_index = 0
    while len(solutions) < VALUES:
        if (composites[current_index] - 1) % minimum_repunit(composites[current_index]) == 0:
            solutions.append(composites[current_index])
        current_index += 1

    # Print the final result
    print sum(solutions)
