"
Problem 3
Largest Prime Factor
"

LOWEST_PRIME = 2
LARGEST_PRIME_OF = 600_851_475_143

# Keep finding primes that divide LARGEST_PRIME_OF until there are no more
prime = 0
decompose = LARGEST_PRIME_OF
current = LOWEST_PRIME
while decompose > 1
  # If it divides, we replace our current largest prime with this one
  prime = current if (decompose % (current += 1)).zero?
  decompose /= current while (decompose % current).zero?
end

# Output the final answer
puts prime
