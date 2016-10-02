"""
Coin Sums
Problem 31
"""
# Calculates the number of ways limit can be made using coins. We assume the
# coins are given sorted by value, from largest to smallest
def change(limit=200, coins=[200, 100, 50, 20, 10, 5, 2, 1]):
    # If there is only one coin left, we return 1 if the coin divides limit,
    # and 0 otherwise, as there is only one potential way to use the coin.
    # Else, we add the number of ways to make the limit using the largest coin,
    # then two of the largest coin, then three, and so on.
    return int(limit % coins[0] == 0) if len(coins) == 1 else \
           sum(change(i, coins[1:]) for i in range(limit, -1, -coins[0]))

print change()
