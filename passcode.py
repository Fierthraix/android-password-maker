#!/usr/bin/env python3

import sys
import random
import argparse


def print_grid(grid):
    for i, row in enumerate(grid):
        print(' '.join(row))


# Returns a coordinate list of unused neighbouring points
def get_neighbours(point, grid, grid_size):
    neighbours = []

    # Iterate over surrounding points
    for i in range(point[0] - 1, point[0] + 2):
        for j in range(point[1] - 1, point[1] + 2):

            # Make sure point is valid
            if 0 <= i < grid_size and 0 <= j < grid_size:
                # Make sure point isn't used already
                if grid[i][j] == 'x':
                    neighbours.append([i, j])

    return neighbours


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("grid_size", help="A number from 3 to 6", default="3",
                    type=int)
    ap.add_argument("pass_len", help="The password length (at least 3 segments)",
                    default="4", type=int)

    args = vars(ap.parse_args())

    grid_size = args["grid_size"]
    pass_len = args["pass_len"]

    if grid_size < 3 or grid_size > 6:
        sys.stderr.write("Android grid sizes are 3x3, 4x4, 5x5, or 6x6")

    if pass_len < 3 or pass_len > grid_size**2:
        sys.stderr.write("Your passphrase must be greater than 3 and not larger than the grid")

    # Produces a grid_size x grid_size matrix
    grid = [['x' for i in range(grid_size)] for i in range(grid_size)]

    # Starting Point
    point = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

    # This loop builds the password and restarts if it gets trapped
    i = 0
    while True:
        # Update the grid with the next password point
        grid[point[0]][point[1]] = str(i+1)

        # Break if the password is the right length
        if i == pass_len - 1:
            print_grid(grid)
            break

        # Get a point's neighbours
        neighbours = get_neighbours(point, grid, grid_size)

        # Restarts in case the pattern can't continue
        if len(neighbours) == 0:
            grid = [['x' for i in range(grid_size)] for i in range(grid_size)]
            point = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
            i = -1

        # If there's only 1 option, take it
        elif len(neighbours) == 1:
            point = neighbours[0]

        # Choose a random neighbour as the next point
        else:
            point = neighbours[random.randint(0, len(neighbours) - 1)]

        i += 1


if __name__ == '__main__':
    main()
