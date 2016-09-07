"""
Concealed Square
Problem 206
"""

# The square ends in a zero, thus necessarily the last digit of the number is
# a zero, and so the second last digit is also a zero. Therefore the number
# is of the form 1_2_3_4_5_6_7_8_900. But then we know that the number
# must end in 30 or 70, to get the trailing 900 in the square. Thus:
#   The square is of the form 1_2_3_4_5_6_7_8_900
#   The number is of the form ...30 or ...70

# We can also start the search from the minimum possible square root, which
# would be sqrt(1020304050607080900) ~ 1010101010, We adjust this to end in
# 30 as required above, and so have the number 1010101030.

# A function that returns true if the number n is the solution
def solution(n):
    n = str(n ** 2)
    return all(int(n[i * 2]) == i + 1 for i in xrange(9))

# Check each number from our starting number, and keep track of the thirty
# and seventy respectively
current = 1010101030
while not solution(current):
    # If we're on an even iteration we add forty to get a trailing 70. Else,
    # we'd like to add sixty so that we get a trailing 30.
    current += 40 if current % 100 == 30 else 60

print current
