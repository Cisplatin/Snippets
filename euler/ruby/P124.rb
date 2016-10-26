"""
Sorted Radicals
Problem 124
"""

INDEX = 10000
UPPER_BOUND = 100001
LOWEST_PRIME = 2

if __FILE__ == $0
  # We run a custom sieve whereby we set each element's radical
  radicals = Array.new(UPPER_BOUND, 1)
  (LOWEST_PRIME...UPPER_BOUND).each do |prime|
    (prime...UPPER_BOUND).step(prime).each{ |n| radicals[n] *= prime } if radicals[prime] == 1
  end

  # Sort the radicals and find the required element
  puts radicals.zip(0...UPPER_BOUND).sort![INDEX].last
end
