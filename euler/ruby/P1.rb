"""
Problem 1
Multiples of 3 and 5
"""

MINIMUM, MAXIMUM = 1, 1000
DIVISORS = [3, 5]

puts (MINIMUM...MAXIMUM) \
    # Filters all numbers not divisible by our numbers
    .select{|n| DIVISORS.any? {|k| n % k == 0} } \
    # Equivalent to reduce(0, +); simply adds all the numbers
    .inject(:+)
