"""
Self-Powers
Problem 48
"""

MIN, MAX = 1, 1000
MODULOS = 10000000000

if __name__ == '__main__':
    # We simply brute force the solution
    print sum((i ** i for i in range(MIN, MAX))) % MODULOS
