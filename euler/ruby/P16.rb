"""
  Power Digit Sum
  Problem 16
"""

BASE, POWER = 2, 1000

# We simply add all the digits after calculating the number
puts (BASE ** POWER).to_s.split('').map(&:to_i).inject(:+)
