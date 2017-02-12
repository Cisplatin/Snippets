"
Problem 4
Largest Palindrome Product
"

NUMBER_BASE = 10
NUM_OF_DIGITS = 3
PRODUCT_DEGREE = 2

# Find the range of numbers we want to work in (the maximum is exclusive)
minimum = NUMBER_BASE ** (NUM_OF_DIGITS - 1)
maximum = minimum * NUMBER_BASE

puts (minimum...maximum)
  .to_a.combination(PRODUCT_DEGREE)        # Find combinations of two numbers
  .map { |n| n.inject(:*) }                # Multiply the numbers together
  .select { |n| n.to_s.reverse.to_i == n } # Filter non-palindrome multiples
  .max                                     # Find the maximum
