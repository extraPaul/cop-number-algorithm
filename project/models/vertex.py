from __future__ import annotations


class Vertex(object):

    @staticmethod
    def get_names(vList: list[Vertex]):
        return list(map(lambda v: v.name, vList))

    # Creates a new vertex with empty edges.
    # @param vName Name of the vertex
    def __init__(self, vName: str):
        self.name = vName
        self.adjacent:list[Vertex] = []

    def add_edge(self, v: Vertex):
        self.adjacent.append(v)

    def is_adjacent(self, v: Vertex):
        if any(x.name == v.name for x in self.adjacent):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
         return self.name + ': ' + str(list(map(lambda v: v.name, self.adjacent)))
    def __str__(self):
         return self.name + ': ' + str(list(map(lambda v: v.name, self.adjacent)))
