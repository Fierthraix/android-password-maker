#!/usr/bin/env python3

import sys
import random

def help_dialog():
    sys.stderr.write('''usage:
        passcode.py [grid_size] [pass_len (number)]

        grid_size: a number from 3 to 6
                
        pass_len: the length of the password (at least 3 segments long)
        ''')

    sys.exit(1)

try:
    grid_size = int(sys.argv[1])
    pass_len = int(sys.argv[2])

    if grid_size < 3 or grid_size > 6:
        raise ValueError("Android grid sizes are 3x3, 4x4, 5x5 or 6x6")

    if pass_len < 3 or pass_len > grid_size**2:
        raise ValueError("Your passphrase must be greater than 3 and not larger than the grid")

except:
    help_dialog()

        
    
# Prints the grid
#def print_grid(grid):
#    for i, row in enumerate(grid):
#        print(' '.join(row))

def print_grid(grid):
    final_grid = []
    for i, row in enumerate(grid):
        print(' '.join(row))

# Returns a coordinate list of unused neighbouring points
def get_neighbours(point):
    neighbours = []

    # Iterate over surrounding points
    for i in range(point[0] - 1, point[0] + 2):
        for j in range(point[1] - 1, point[1] + 2):

            # Make sure point is valid
            if 0 <= i < grid_size and 0 <= j < grid_size:

                # Make sure point isn't used already
                if grid[i][j] == 'x':

                    neighbours.append([i,j])

    return neighbours

# Produces a grid_size x grid_size matrix
grid = [ [ 'x' for i in range(grid_size) ] for i in range(grid_size) ]

# Starting Point
point = [ random.randint(0, grid_size - 1), random.randint(0, grid_size - 1) ]

# This loop builds the password and restarts if it gets trapped
i = 0
while True:
    # Update the grid with the next password point
    grid[ point[0] ][ point[1] ] = str(i+1)

    # Break if the password is the right length
    if i == pass_len - 1:
        print_grid(grid)
        break

    # Get a point's neighbours
    neighbours = get_neighbours(point)

    # Restarts in case the pattern can't continue
    if len(neighbours) == 0:
        grid = [ [ 'x' for i in range(grid_size) ] for i in range(grid_size) ]
        point = [ random.randint(0, grid_size - 1), random.randint(0, grid_size - 1) ]
        i = -1

    # If there's only 1 option, take it
    elif len(neighbours) == 1:
        point = neighbours[0]

    # Choose a random neighbour as the next point
    else:
        point = neighbours[ random.randint(0, len(neighbours) - 1) ]

    i += 1
