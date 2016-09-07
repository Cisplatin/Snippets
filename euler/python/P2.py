"""
Even Fibonacci Numbers
Problem 2
"""

MAX = 4000000
f_0, f_1 = 0, 1

def fibonacci(f_n, f_m):
    # Generates all fibonacci numbers with value below MAX. Assume f_n is
    # the nth fibonacci number and f_m is the (n+1)th fibonacci number
    while f_m < MAX:
        f_n, f_m = f_m, f_n + f_m

        # Filter out the odd elements of the generator
        if f_n % 2 == 0:
            yield f_n

if __name__ == '__main__':
    # Print out the sum
    print sum(fibonacci(f_0, f_1))
