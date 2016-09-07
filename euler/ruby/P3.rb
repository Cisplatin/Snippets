"""
Problem 3
Largest Prime Factor
"""

LARGEST_PRIME_OF = 600851475143
LOWEST_PRIME = 2

# Keep finding primes that divide LARGEST_PRIME_OF until there are no more
primes, decompose, current = [], LARGEST_PRIME_OF, LOWEST_PRIME
while decompose > 1 && current <= Math.sqrt(decompose)
    # If it divides, we add it to our list of primes
    if decompose % current == 0
        primes.push(current)
        while decompose % current == 0
            decompose /= current
        end
    end
    current += 1
end

# If at the end, decompose is still not 1, then decompose is another prime.
# However, since we only care about the max, we can just append decompose and
# skip an if-statement, as there will always be a prime larger than 1
puts (primes + [decompose]).max
