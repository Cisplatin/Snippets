"""
Problem 3
Largest Prime Factor
"""

LARGEST_PRIME_OF = 600851475143
LOWEST_PRIME = 2

# Keep finding primes that divide LARGEST_PRIME_OF until there are no more
prime, decompose, current = 0, LARGEST_PRIME_OF, LOWEST_PRIME
while decompose > 1
    # If it divides, we replace our current largest prime with this one
    prime = current if decompose % (current += 1) == 0
    decompose /= current while decompose % current == 0
end

# Output the final answer
puts prime
