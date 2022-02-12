from __future__ import annotations
from project.models.vertex import Vertex


class Combination(object):
    # Creates a new vertex with empty edges.
    # @param vName Name of the vertex
    def __init__(self, v1: Vertex, v2: Vertex, is_cop=False):
        self.v1 = v1
        self.v2 = v2
        self.cop_turn = is_cop
        self.marked = False
        self.name = v1.name + v2.name + ("-Cop" if is_cop else "-Rob")
        self.adjacent:list[Combination] = []

    def add_edge(self, c: Combination):
        self.adjacent.append(c)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
         return "Combination(" + self.name + ", marked: " + str(self.marked) + ", adj:" + str(list(map(lambda v: v.name, self.adjacent))) + ")"
    def __str__(self):
         return "Combination(" + self.name + ", marked: " + str(self.marked) + ", adj:" + str(list(map(lambda v: v.name, self.adjacent))) + ")"


class MultiCombination(object):
    # Creates a new vertex with empty edges.
    # @param vName Name of the vertex
    def __init__(self, cops: list[Vertex], rober: Vertex, is_cop=False, force_movement=False):
        self.cops = cops
        self.rober = rober
        self.cop_turn = is_cop
        self.marked = False
        self.adjacent:list[MultiCombination] = []

        self.name = ""
        for c in cops:
            self.name += c.name

        self.name += (rober.name + ("-Cop" if is_cop else "-Rob"))

    def add_edge(self, c: MultiCombination):
        self.adjacent.append(c)

    def check_cops_equal(self, c: MultiCombination):
        for i in range(len(self.cops)):
            if self.cops[i] != c.cops[i]:
                return False

        return True


    def check_existing_adjascent_cops(self, c: MultiCombination):
        """ Return true if at least one of the cops has moved, and it is at an adjascent spot"""

        diff = [] # list of index
        for i in range(len(self.cops)):
            if self.cops[i] != c.cops[i]:
                diff.append(i)

        if len(diff) < 1:
            return False

        # Return false if any of the moves were not to an adjacent cop
        if any((not self.cops[i].is_adjacent(c.cops[i])) for i in diff):
            return False
        else:
            return True


    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
         return "MultiCombo(" + self.name + ", marked: " + str(self.marked) + ", adj:" + str(list(map(lambda v: v.name, self.adjacent))) + ")"
    def __str__(self):
         return "MultiCombo(" + self.name + ", marked: " + str(self.marked) + ", adj:" + str(list(map(lambda v: v.name, self.adjacent))) + ")"
