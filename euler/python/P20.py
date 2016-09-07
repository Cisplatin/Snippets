"""
Factorial Digit Sum
Problem 20
"""

from math import factorial

if __name__ == '__main__':
    # Python makes life so easy. We just calculate the 100th factorial.
    print sum([int(i) for i in str(factorial(100))])
