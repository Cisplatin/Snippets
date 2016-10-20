"""
  Sum Square Difference
  Problem 6
"""

MINIMUM = 1
MAXIMUM = 100

puts (MINIMUM..MAXIMUM).inject(:+) ** 2 - (MINIMUM..MAXIMUM).map{ |i| i ** 2 }.inject(:+)
