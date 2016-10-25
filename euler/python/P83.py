"""
Path sum: Four ways
Problem 83
"""

MATRIX_TXT = "P83.txt"
DIMENSIONS = 80

from itertools import product

if __name__ == '__main__':
    # Make the matrix readable
    matrix = map(lambda x: map(int, x[:-1].split(",")), open(MATRIX_TXT, 'r').readlines())

    # Returns the matrix value of the given node
    def matrix_value(node):
        return matrix[node[0]][node[1]]

    # We create an implementation of Djikstra's algorithm
    unvisited = list(product(xrange(0, DIMENSIONS), repeat=2))
    distance = {node : '' if node != (0, 0) else matrix_value(node) for node in unvisited}
    while unvisited:
        # Get the node with the smallest value
        node_distance, node = min((distance[node], node) for node in unvisited)
        unvisited.remove(node)

        # Check each neighbour for a smaller path
        for increment in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            other_node = tuple(sum(i) for i in zip(node, increment))
            if other_node in distance:
                path = node_distance + matrix_value(other_node)
                distance[other_node] = min(path, distance[other_node])

    # Print out the minimum value
    print distance[(DIMENSIONS - 1, DIMENSIONS - 1)]
