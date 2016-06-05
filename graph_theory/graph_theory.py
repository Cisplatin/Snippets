class Graph:
    """
    A class used to represent mathematical graphs.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Adds the given vertex to the graph.
        Raises an error if the vertex already exists.
        """
        if vertex in self.graph:
            raise ValueError("Vertex '%s' already exists." % vertex)
        self.graph[vertex] = []

    def connect_directed(self, vertex_1, vertex_2):
        """
        Connects the given vertices with a directed edge. Specifically, an edge
        from vertex_1 that leads to vertex_2.
        Raises an error if one of the vertices don't exist
        """
        if not vertex_1 in self.graph:
            raise ValueError("Vertex '%s' does not exist." % vertex_1)
        if not vertex_2 in self.graph:
            raise ValueError("Vertex '%s' does not exist." % vertex_2)
        self.graph[vertex_1].append(vertex_2)

    def connect_undirected(self, vertex_1, vertex_2):
        """
        Connects the given vertices with an undirected edge.
        """
        if not vertex_1 in self.graph:
            raise ValueError("Vertex '%s' does not exist." % vertex_1)
        if not vertex_2 in self.graph:
            raise ValueError("Vertex '%s' does not exist." % vertex_2)
        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)
