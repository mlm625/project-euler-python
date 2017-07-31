#
# Lattice paths
# Problem 15
#
# Starting in the top left corner of a 2x2 grid, and only being
# able to move to the right and down, there are exactly 6 routes
# to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?
#


X = 20
Y = 20

GRID = [X, Y]

# can only move forward or upward by 1.
MOVES = [1, 1]


def routes(grid, moves):

    if grid == [0, 0]:
        return 1

    total = 0
    if grid[0] > 0:
        total += routes([grid[0] - moves[0], grid[1]], moves)

        if grid[1] > 0:
            total += routes([grid[0], grid[1] - moves[1]], moves)

    return total


def main():
    print("Number of routes: {}".format(2 * routes(GRID, MOVES)))


if __name__ == '__main__':
    main()

