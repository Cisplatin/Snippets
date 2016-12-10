"""
Cyclical Figurate Numbers
Problem 61
"""

BASE = 10
DIGITS = 4
MATCHERS = 2
MINIMUM_POLYGONAL = 3
MAXIMUM_POLYGONAL = 8

# Returns all s-gonal numbers with four digits
def generate_n_gonals(s):
    MINIMUM, MAXIMUM = BASE ** (DIGITS - 1), BASE ** DIGITS
    n, current = 0, 0
    while current < MAXIMUM:
        if current >= MINIMUM:
            yield str(current)
        n += 1
        # This is generated based off of the generalized polygonal formula
        current = (n * n * (s - 2) - n * (s - 4)) / 2

# Genereates a list of all different polygonal types as strings
def generate_polygonals():
    return [list(generate_n_gonals(i)) for i in xrange(MINIMUM_POLYGONAL, MAXIMUM_POLYGONAL + 1)]
polygonals = generate_polygonals()

# Returns true if the two given elements are connectors (in the order given)
def connector(n, m):
    return n[-MATCHERS:] == m[:MATCHERS]

# This is the implementation of the DFS on path
def find_cyclic_path(current_path, unvisited):
    # If our path has been found, make sure the last and first element match
    if unvisited == []:
        if connector(current_path[-1], current_path[0]):
            return current_path

    # Otherwise we go through each possible other node and try to connect
    for gonal in unvisited:
        for node in polygonals[gonal]:
            if connector(current_path[-1], node):
                next_unvisited = filter(lambda x: x != gonal, unvisited)
                new_path = find_cyclic_path(current_path + [node], next_unvisited)
                if new_path != None:
                    return new_path

# Returns the full cycle on the graph
def find_complete_cycle():
    # The last polygonal group will be the smallest due to increased spacing, and so we use those
    # as our starting nodes, and attempt to brute-force each possibility
    for start in polygonals[-1]:
        # Try to find a path via a depth-first search
        cycle = find_cyclic_path([start], range(MAXIMUM_POLYGONAL - MINIMUM_POLYGONAL))
        if cycle != None:
            return cycle

if __name__ == '__main__':
    print sum(map(int, find_complete_cycle()))
