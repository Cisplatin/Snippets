"""
Problem 2
Even Fibonacci Numbers
"""

MAXIMUM = 4000000

# We create a fibonacci enumerator so that we can lazily generate them
fibonacci = Enumerator.new do |y|
  n = m = 1
  loop do
    y << n
    n, m = m, n + m
  end
end

# Sum all the numbers that are event
puts fibonacci.take_while{|i| i < MAXIMUM}.select{|x| x.even?}.inject(:+)
