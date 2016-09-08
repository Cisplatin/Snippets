"""
Problem 4
Largest Palindrome Product
"""

# We use pure functional programming. Pretty read-able, but the gist is that
# it takes every combonation of two-digit numbers, multiplies it, then finds
# the maximal result.
puts (100..999).to_a.combination(2).map{|n| n.inject(:*)}.select{|n| n.to_s.reverse.to_i == n}.max
