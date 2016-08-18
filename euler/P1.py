# Multiples of 3 and 5
# Problem 1

if __name__ == '__main__':
    # Generates all numbers from 0 to 999 that are a multiple of
    # 3 or a multiple of 5 (inclusively), and prints the sum
    print sum(i for i in range(1000) if not (i % 3 and i % 5))
