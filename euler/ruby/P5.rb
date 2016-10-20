"""
  Smallest Multiple
  Problem 5
"""

MINIMUM = 1
MAXIMUM = 20

puts (MINIMUM...MAXIMUM).inject(&:lcm)
