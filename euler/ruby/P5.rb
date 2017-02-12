"
Smallest Multiple
Problem 5
"

MINIMUM = 1
MAXIMUM = 20

# The smallest positive number that divides all the numbers requested is
# equivalent to the lowest common multiplier
puts (MINIMUM...MAXIMUM).inject(&:lcm)
