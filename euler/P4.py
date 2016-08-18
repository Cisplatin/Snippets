"""
Largest Palindrome Product
Problem 4
"""

MIN, MAX = 100, 999

if __name__ == '__main__':
    # Generate a list of all products of two three-digit numbers
    numbers = [i * j for i in range(MIN, MAX) for j in range(MIN, i)]
    # Filter out non-palindromes and print the maximum
    numbers = filter(lambda x: str(x) == str(x)[::-1], numbers)
    print max(numbers)

