#
# solve problem 31 with memoization, bottoms up approach.
#

# list of the 8 available denominations in pence.
COINS = [1, 2, 5, 10, 20, 50, 100, 200]
NUM_COINS = len(COINS)

CHANGE = 200

# array representing graph and path count, with index as nodes and value as number of ways to get from
# start (node[CHANGE]) to end (node 0).
WAYS_TABLE = [0] * (CHANGE+1)

# At node 0, there's 1 way to get to node 0.
WAYS_TABLE[0] = 1


def count_ways(change, coins):
    # treat each coin as a edge between the nodes and see if there's a way to get from start to end
    # using that coin.
    for index in range(0, NUM_COINS):
        # walk graph by starting with node closet to end given the coin value.
        for amount in range(coins[index], change + 1):
            # walk the graph with new coin, i.e. move to the next node by subtracting the coin
            # amount and get the path count for the new node to end.
            WAYS_TABLE[amount] += WAYS_TABLE[amount - coins[index]]

    return WAYS_TABLE[change]


def main():
    count_ways(CHANGE, COINS)

    print("Ways to make change for {}: {}".format(CHANGE, WAYS_TABLE[CHANGE]))

    print(WAYS_TABLE)


if __name__ == '__main__':
    main()