"
Problem 2
Even Fibonacci Numbers
"

MAXIMUM = 4_000_000

# We create a fibonacci enumerator so that we can lazily generate them.
# f_n and f_m are the f_nth and f_mth fibonacci numbers.
fibonacci = Enumerator.new do |next_element|
  f_n = f_m = 1
  loop do
    next_element << f_n
    f_n, f_m = f_m, f_n + f_m
  end
end

puts fibonacci.take_while { |i| i < MAXIMUM }.select(&:even?).inject(:+)
