"""
Problem 2
Even Fibonacci Numbers
"""

F_0, F_1 = 1, 1
MAXIMUM = 4000000

# We generate each fibonacci number under we hit our maximum
sum, f_n, f_m = 0, F_0, F_1
while f_n < MAXIMUM
    f_n, f_m = f_m, f_n + f_m
    # Only add the even numbers we come across
    sum += f_n % 2 == 0 ? f_n : 0
end
puts sum
