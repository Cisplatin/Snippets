"""
Prime Pair Set
Problem 60
"""

UPPER_BOUND = 10000
FAMILY_SIZE = 5
LOWEST_PRIME = 2

from itertools import product
from math import sqrt

if __name__ == '__main__':
    # Returns true if the given number is prime
    existence = {}
    def check_if_prime(prime):
        if prime not in existence:
            existence[prime] = all(prime % i != 0 for i in xrange(LOWEST_PRIME, int(sqrt(prime))))
        return existence[prime]

    # We check the concatenation property for each prime
    concatenation = {}
    def valid_property(prime_1, prime_2):
        if (prime_1, prime_2) not in concatenation:
            valid = check_if_prime(int(str(prime_1) + str(prime_2))) and \
                    check_if_prime(int(str(prime_2) + str(prime_1)))
            concatenation[(prime_1, prime_2)] = valid and prime_1 != prime_2
        return concatenation[(prime_1, prime_2)]

    # Sieve for primes with an arbitrary upper bound and see if we can find the family
    prime_set, primes, current_family, sieve = set(), [], [], [True] * UPPER_BOUND
    for prime in xrange(LOWEST_PRIME, UPPER_BOUND):
        if sieve[prime]:
            for other in primes:
                if valid_property(prime, other):
                    current_family.append(set([prime, other]))
                    prime_set |= set([prime, other])
            primes.append(prime)
            existence[str(prime)] = True
            for composite in xrange(prime * prime, UPPER_BOUND, prime):
                sieve[composite] = False

    # Keep forming families until we reach the family size or we run out of formations.
    # We subtract two because we found pairs above.
    for i in xrange(FAMILY_SIZE - 2):
        # We compare each prime to each family it's not in and create a new family
        new_family = []
        new_prime_set = set()
        for prime, family in product(prime_set, current_family):
            new_set = set([prime]) | family
            if all(valid_property(prime, i) for i in family) and new_set not in new_family:
                new_family.append(new_set)
                new_prime_set |= new_set
        current_family = new_family
        prime_set = new_prime_set

        # If there are no more families to create, we need a higher upper bound
        if current_family == []:
            raise Exception("Could only find families of size %s with given UPPER_BOUND." % (i + 1))

    # Print the minimum set
    print min(map(sum, current_family))
