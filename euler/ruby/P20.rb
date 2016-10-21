"""
  Factorial Digit Sum
  Problem 20
"""

NUMBER = 100

# We simply calculate the factorial and sum the digits
puts (1..NUMBER).inject(:*).to_s.split('').map(&:to_i).inject(:+)
