#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label, color="white"):
        self.label = label
        self.edges = set()
        self.color = color

    def __repr__(self):
        return str(self.label)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    #Adjacency list graph
    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)


lg = Graph()

v1 = Vertex("v 1")
lg.add_vertex(v1)
v2 = Vertex("v 2")
lg.add_vertex(v2)
v3 = Vertex("v 3")
lg.add_vertex(v3)
v4 = Vertex("v 4")
lg.add_vertex(v4)


lg.add_edge(v1, v2)
lg.add_edge(v2, v4)
lg.add_edge(v3, v4)
lg.add_edge(v4, v1)
