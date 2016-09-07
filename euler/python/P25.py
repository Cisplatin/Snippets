"""
1000-digit Fibonacci Number
Probelm 25
"""

DIGITS = 1000
f_0, f_1 = 1, 1

if __name__ == '__main__':
    # We generate each fibonacci number and check the length
    f_n, f_m, index = f_0, f_1, 1
    while(len(str(f_n)) < DIGITS):
        f_n, f_m = f_m, f_n + f_m
        index += 1

    # Print the index of the f_n fibonacci number
    print index
