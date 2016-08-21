"""
Consecutive Prime Sum
Problem 50
"""

MIN_PRIME, MAX_PRIME = 2, 1000000

def sieve():
    # Runs the sieve of eratosthenes to find prime numbers up to MAX_PRIME
    erato, primes, exists = [True] * MAX_PRIME, [], {}
    for i in range(MIN_PRIME, MAX_PRIME):
        if erato[i]:
            primes.append(i)
            exists[i] = True
            for j in range(i, MAX_PRIME, i):
                erato[j] = False
    return (primes, exists)


if __name__ == '__main__':
    # Sieve all primes to a million, and then only look for the largest sum
    primes, exists = sieve()

    # Find the index at which the sum of the primes exceeds MAX_PRIME
    def find_prime():
        for length in range(len(primes) / 10, 0, -1):
            # Given that the longest then for MAX_PRIME = 1000 is 21, we can
            # assume that the longest chain for MAX_PRIME = 1000000 won't be
            # over a hundred-thousand (maybe incorrectly so, but meh it worked)
            for start in range(0, len(primes) - length - 1):
                current_sum = sum(primes[start:start + length])
                if current_sum in exists:
                    return current_sum
                elif current_sum > MAX_PRIME:
                    break
    print find_prime()
