#!/usr/bin/python3

"""determine the few number of coins needed to meet the total"""

def makeChhange(coin, total):
    """
    Return: fewest number of coins needed to meet total
        if total is 0 or less return 0
        if total cannot be meet by number of coins you return 1
    """

    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
