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

# create matrix
GRID = [[0 for i in range(X+1)] for j in range(Y+1)]


# can only move forward or upward by 1.
MOVES = [1, 1]


def routes(grid):
    # There's only 1 path from 0,Y or X,0 to X,Y.
    for x in range(X+1):
        grid[x][0] = 1
        grid[0][x] = 1

    # Bottom up approach:
    #   the number of paths to a coordinate is the sum of the paths to the direct predecessor coordinates.
    for x in range(1, X+1):
        for y in range(1, Y+1):
            grid[x][y] = grid[x-1][y] + grid[x][y-1]

    return grid[X][Y]


def main():
    print("Number of routes: {}".format(routes(GRID)))

    for x in range(0, X+1):
        print(GRID[x])


if __name__ == '__main__':
    main()
