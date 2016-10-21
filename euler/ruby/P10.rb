"""
  Summation of Primes
  Problem 10
"""

require 'prime'

MAXIMUM = 2000000

puts Prime.take_while{ |i| i < MAXIMUM }.inject(:+)
