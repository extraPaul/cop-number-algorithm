from project.models.combination import Combination, MultiCombination
from project.models.vertex import Vertex

# VERSION WITH OBJECTS
class Graph(object):
    # Creates a new vertex with empty edges.
    # @param vName Name of the vertex
    def __init__(self, directed=False):
        self.vList:list[Vertex] = []
        self.directed = directed

    def add_vertex(self, v: Vertex):
        self.vList.append(v)

    def create_vertex(self, vName: str):
        vtx = Vertex(vName)
        self.vList.append(vtx)

    def add_edge(self, v1: Vertex, v2: Vertex):
        v1.add_edge(v2)
        if not self.directed:
            v2.add_edge(v1)

    def get_key_list(self):
        return list(map(lambda x: x.name, self.vList))

    def find_by_name(self, name: str) -> Vertex:
        return next(v for v in self.vList if v.name == name)

    def __repr__(self):
         return "Graph() object"
    def __str__(self):
         return "Graph(" + str(self.vList) + ")"

# VERSION WITH STRINGS
# class Graph(object):
#     # Creates a new vertex with empty edges.
#     # @param vName Name of the vertex
#     def __init__(self, verteces:dict[str, list[str]]=[], directed=False):
#         self.vList = verteces
#         self.directed = directed

#     def add_vertex(self, v: str):
#         self.vList[v] = []

#     def add_edge(self, v1: str, v2: str):
#         self.vList[v1].append(v2)
#         if not self.directed:
#             self.vList[v2].append(v1)


class ComboGraph(object):
    # Creates a new vertex with empty edges.
    # @param vName Name of the vertex
    def __init__(self, directed=True):
        self.vList:list[Combination] = []
        self.directed = directed

    def add_vertex(self, c: Combination):
        self.vList.append(c)

    def add_edge(self, c1: Combination, c2: Combination):
        c1.add_edge(c2)
        if not self.directed:
            c2.add_edge(c1)

    def marked_list(self):
        return list(filter(lambda v: v.marked, self.vList))

    def unmarked_list(self):
        return list(filter(lambda v: not v.marked, self.vList))

    def cop_list(self):
        return list(filter(lambda v: v.cop_turn, self.vList))

    def rober_list(self):
        return list(filter(lambda v: not v.cop_turn, self.vList))

    def __repr__(self):
         return "ComboGraph() object"
    def __str__(self):
        retVal = "ComboGraph(\n"

        for v in self.vList:
            retVal += str(v) + ("\t" if v.cop_turn else "\n")

        return retVal + ")"

class MultiComboGraph(object):
    # Creates a new vertex with empty edges.
    # @param vName Name of the vertex
    def __init__(self, directed=True, force_movement=False):
        self.vList:list[MultiCombination] = []
        self.directed = directed

        # This relates to the type of game.
        # In the first version of the game, we have the choice to move or stay put.
        # In the second version of the game, we are forced to move.
        self.force_movement = force_movement

    def add_vertex(self, c: MultiCombination):
        self.vList.append(c)

    def add_edge(self, c1: MultiCombination, c2: MultiCombination):
        c1.add_edge(c2)
        if not self.directed:
            c2.add_edge(c1)

    def marked_list(self):
        return list(filter(lambda v: v.marked, self.vList))

    def unmarked_list(self):
        return list(filter(lambda v: not v.marked, self.vList))

    def cop_list(self):
        return list(filter(lambda v: v.cop_turn, self.vList))

    def rober_list(self):
        return list(filter(lambda v: not v.cop_turn, self.vList))

    def check_legal_cop_move(self, c1: MultiCombination, c2: MultiCombination):
        """ Return true if a move from c1 to c2 is legal for a cop, and false otherwise. This depends on the version of the game."""

        # Here c1 is a cop turn, and c2 is the rober turn
        if self.force_movement:
            return c1.check_existing_adjascent_cops(c2)
        else:
            return (c1.check_cops_equal(c2) or c2.check_existing_adjascent_cops(c1))

    
    def check_legal_rober_move(self, c1: MultiCombination, c2: MultiCombination):
        """ Return true if a move from c1 to c2 is legal for a cop, and false otherwise. This depends on the version of the game."""

        # Here c1 is a cop turn, and c2 is the rober turn
        if self.force_movement:
            return c2.check_existing_adjascent_cops(c1)
        else:
            return (c1.rober == c2.rober or c1.rober.is_adjacent(c2.rober))


    def __repr__(self):
         return "MultiComboGraph() object"
    def __str__(self):
        retVal = "MultiComboGraph(\n"

        for v in self.vList:
            retVal += str(v) + ("\t" if v.cop_turn else "\n")

        return retVal + ")"
