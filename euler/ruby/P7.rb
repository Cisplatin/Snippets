"
10001st Prime
Problem 7
"

require 'prime'

PRIME_INDEX = 10_001

# Simply take the first PRIME_INDEX prime numbers from the enumerator, then
# take the last one
puts Prime.take(PRIME_INDEX).last
