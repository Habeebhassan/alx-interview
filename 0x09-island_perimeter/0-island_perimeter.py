#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculates the perimeter of the island in a given grid.

    Args:
        grid (list): A list of lists containing
        integers where 0 represents water and
        1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a cell that is land (1)
                perimeter += 4

                # Check for neighboring cells (up, down, left, right)
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 2

    return perimeter
