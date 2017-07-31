# # -*- coding: utf-8 -*-
#
# Coin sums
# Problem 31
#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in
# general circulation:
#
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
#
# It is possible to make £2 in the following way:
#
#   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?
#

# list of the 8 available denominations in pence.
COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def count_ways(change, index, coins):
    # negative change, this combination of coins do not work.
    if change < 0:
        return 0

    # ran out of coins, this combination does not work.
    if index >= 8:
        return 0

    # print("change: {}, coin: {}".format(change, coins[index]))
    # change is 0, found a combination of coins that worked.
    if change == 0:
        # print("found way")
        return 1

    #
    # There change remaining so keep recursing. Skip coins already used in combinations
    # before so only unique combinations are counted.
    #

    total = 0
    if index < 7 and change >= coins[index+1]:
        # skip this coin and see how many ways to make change without using this denomination.
        total = count_ways(change, index+1, coins)

    if change >= coins[index]:
        # use this coin in making change and see how how many ways to make change for the
        # smaller amount.
        total += count_ways(change-coins[index], index, coins)

    return total

    # remove duplicate patterns by either using a coin in the solution or not using it.
    #return count_ways(change, index+1, coins) + count_ways(change-coins[index], index, coins)

    # counts ALL the ways, not unique ways.
    #return sum([count_ways(change - coin, coins) for coin in coins if change >= coin])


def main():
    change = 300
    print("Ways to make change for {}: {}".format(change, count_ways(change, 0, COINS)))


if __name__ == '__main__':
    main()
