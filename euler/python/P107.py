"""
Minimal Network
Problem 107
"""

NETWORK_TXT = 'P107.txt'

if __name__ == '__main__':
    # We first parse the text file. We create a set of edges that are defined as 3-tuples with
    # the first element being an integer weight, and the second and third elements being
    # the vertices connected. Vertices are numbered numerically
    with open(NETWORK_TXT, 'r') as f:
        rows = map(lambda x: x[:-1].split(','), f.readlines())
        total_weight, vertex_count, edges = 0, len(rows), []
        for row_index, row in enumerate(rows):
            # As to avoid duplication, we only append edges where the column index is
            # less than the row index
            for col_index, weight in enumerate(row[:row_index]):
                if weight != '-':
                    edges.append((int(weight), row_index, col_index))
                    total_weight += int(weight)

    # We use Kruskal's algorithm to go through each edge (in a sorted order by weight) and check
    # if it adds a new portion of the minimum spanning tree. We assume that the graph is 1-connected
    trees, edges = {i : i for i in xrange(vertex_count)}, sorted(edges, reverse=True)

    # We add the new edge only if it adds to the graph. We keep an inefficient union-find data
    # structure to keep track of disconnected trees.
    unique_tree_count = vertex_count
    def add_new_edge(weight, vertex_1, vertex_2):
        if trees[vertex_1] == trees[vertex_2]:
            return 0
        old_tree = trees[vertex_1]
        for vertex in trees:
            if trees[vertex] == old_tree:
                trees[vertex] = trees[vertex_2]

        # Set the new tree count so that we know when we have a spanning tree
        global unique_tree_count
        unique_tree_count = len(set(trees.values()))
        return weight

    # We subtract the total weight by each edge found to result in the total savings
    while unique_tree_count > 1:
        total_weight -= add_new_edge(*edges.pop())
    print total_weight
