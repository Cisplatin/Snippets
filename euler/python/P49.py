"""
Prime Permutations
Problem 49
"""

BASE = 10
KNOWN = '148748178147'
PRIME_LENGTH = 4
PERMUTATIONS = 3

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to upper_bound
    upper_bound = BASE ** PRIME_LENGTH
    erato, primes = [True] * upper_bound, []
    for i in range(2, upper_bound):
        if erato[i]:
            # We found a prime, so switch off all multiples
            primes.append(str(i))
            for j in range(i, upper_bound, i):
                erato[j] = False
    return primes

if __name__ == '__main__':
    # First we get a list of all primes that are PRIME_LENGTH-digits long
    primes = filter(lambda x: len(x) == PRIME_LENGTH, sieve())

    # We then check for permutations of each and only keep those that have
    # at least two permutations
    checked_primes = {}
    sorted_primes = map(lambda x: ''.join(sorted(x)), primes)
    for i in range(len(primes)):
        # We make passed prime permutations so we don't check them twice
        if i in checked_primes:
            continue

        # Make a list of permutations for each prime
        perm = []
        for j in range(len(primes)):
            if sorted_primes[i] == sorted_primes[j]:
                checked_primes[j] = True
                perm.append(primes[j])

        # If we found at least three, check for sequencing
        solutions = []
        if len(perm) >= PERMUTATIONS:
            perm = map(int, perm)
            for i in range(len(perm)):
                for j in range(i + 1, len(perm)):
                    for k in range(j + 1, len(perm)):
                        if perm[i] - perm[j] == perm[j] - perm[k]:
                            solutions.append("%s%s%s" % (perm[i], perm[j], perm[k]))

        # Print solutions if not the known one
        for solution in solutions:
            if solution != KNOWN:
                print solution
