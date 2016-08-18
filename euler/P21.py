"""
Amicable Numbers
Problem 21
"""

UPPER_BOUND = 10000

if __name__ == '__main__':
    # Check each number up to the UPPER_BOUND for divisors
    total, sum_of_divisors = 0, {0 : 0}
    for i in range(1, UPPER_BOUND):
        # Sum all the proper divisors
        sum_of_divisors[i] = sum([j for j in range(1, i) if i % j == 0])
        # If an amicable pair is found then add to total
        if sum_of_divisors[i] < i and sum_of_divisors[sum_of_divisors[i]] == i:
            total += sum_of_divisors[i] + i
    print total

