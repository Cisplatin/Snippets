"
Problem 1
Multiples of 3 and 5
"

RANGE = (1...1000)
DIVISORS = [3, 5].freeze

puts RANGE.select { |n| DIVISORS.any? { |k| (n % k).zero? } }.inject(:+)
