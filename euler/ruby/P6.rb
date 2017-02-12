"
Sum Square Difference
Problem 6
"

MINIMUM = 1
MAXIMUM = 100

# Calculate the square of the sum and the sum of the squares seperately, then
# print out the difference. We know that the square of the sum will be larger
# so we subtract from that number.
square_of_sum = (MINIMUM..MAXIMUM).inject(:+) ** 2
sum_of_square = (MINIMUM..MAXIMUM).map { |i| i ** 2 }.inject(:+)
puts square_of_sum - sum_of_square
