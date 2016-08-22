"""
Maximum Path Sum II
Problem 67
"""

TRIANGLE_TXT = "P67.txt"

if __name__ == '__main__':
    # We first make the file read-able
    with open(TRIANGLE_TXT, 'r') as f:
        grid = [map(int, i.split(' ')) for i in f.read().split('\n')[:-1]][::-1]

    # If we start from the second bottom row, there is one obvious choice
    # for the maximal path. We use this logic to work backwards up the
    # triangle and find the largest path
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += max(grid[i - 1][j], grid[i - 1][j + 1])
    print grid[-1][-1]
