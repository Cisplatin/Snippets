"""
Coin Sums
Problem 31
"""

COINS = [200, 100, 50, 20, 10, 5, 2, 1]

# Calculates the number of ways limit can be made using coins. We assume the
# coins are given sorted by value, from largest to smallest
memoize = {}
def change(limit, coin=0):
    coin_key = (limit, coin)
    # Check if we've already done this calculation, so we can save it
    if not coin_key in memoize:
        # If there is only one coin left, we return 1 if the coin divides limit,
        # and 0 otherwise, as there is only one potential way to use the coin.
        if coin == len(COINS) - 1:
            memoize[coin_key] = int(limit % COINS[coin] == 0)
        # Else, we add the number of ways to make the limit using the largest coin,
        # then two of the largest coin, then three, and so on.
        else:
            limit_values = xrange(limit, -1, -COINS[coin])
            memoize[coin_key] = sum(change(i, coin + 1) for i in limit_values)
    return memoize[coin_key]

print change(200)
