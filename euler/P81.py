"""
Path Sum: Two Ways
Problem 81
"""

MATRIX_TXT = "P81.txt"

if __name__ == '__main__':
    # Load up the file and make it read-able
    with open(MATRIX_TXT, 'r') as f:
        grid = [map(int, i.split(",")) for i in f.read().split("\n")[:-1]]

    # Find the miniumum sum by going backwards through the matrix, from the
    # bottom right to the top left, keeping track of minimal paths
    for row in reversed(range(len(grid))):
        for col in reversed(range(len(grid[0]))):
            # We set the options to strings, since min(str, int) = int, and
            # specifically the 0-string so that if they are both '0', we add
            # 0 to the cell
            path_1 = grid[row + 1][col] if row + 1 < len(grid) else '0'
            path_2 = grid[row][col + 1] if col + 1 < len(grid) else '0'
            grid[row][col] += int(min(path_1, path_2))
    print grid[0][0]
