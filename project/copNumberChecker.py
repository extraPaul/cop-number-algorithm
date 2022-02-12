

from project.models.combination import Combination, MultiCombination
from project.models.graph import ComboGraph, Graph, MultiComboGraph

import itertools


class CopNumberChecker:
    @staticmethod
    def checkCopNumber1(g: Graph):
        # first define the lists of combinations

        cmbGraph = ComboGraph()

        for u in g.vList:
            for v in g.vList:
                cmb1 = Combination(u, v, True)
                cmb2 = Combination(u, v, False)
                if u == v:
                    cmb1.marked = True
                    cmb2.marked = True

                cmbGraph.add_vertex(cmb1)
                cmbGraph.add_vertex(cmb2)

      
        # Add all the edges in the combo graph
        for cmb in cmbGraph.vList:
            if cmb.cop_turn:
                # Find all combinations where u has an edge to u'
                adjacent = [x for x in cmbGraph.vList if (not x.cop_turn and x.v2 == cmb.v2 and (x.v1 == cmb.v1 or x.v1.is_adjacent(cmb.v1)))]

                for combo in adjacent:
                    cmb.add_edge(combo)
            else:
                # This is a rober turn
                adjacent = [x for x in cmbGraph.vList if x.cop_turn and x.v1 == cmb.v1 and (x.v2 == cmb.v2 or x.v2.is_adjacent(cmb.v2))]

                for combo in adjacent:
                    cmb.add_edge(combo)

        print(cmbGraph)

        newMarked = True
        iterations = 0
        while newMarked:
            iterations += 1
            newMarked = False

            unmarkedCombos = cmbGraph.unmarked_list()

            for c in unmarkedCombos:
                if c.cop_turn:
                    #if there's a neighbour that's marked, mark this
                    markedNeighbor = next((x for x in c.adjacent if x.marked), None)
                    if markedNeighbor is not None:
                        c.marked = True
                        newMarked = True
                else:
                    # This is a rober turn
                    # if all neighbours are marked, mark this one. If there are no unmarked neighbours, they're all marked
                    unmarkedNeighbor = next((x for x in c.adjacent if not x.marked), None)

                    if unmarkedNeighbor is None:
                        c.marked = True
                        newMarked = True

        print("\n=============== AFTER MARKING =================")
        print("Iterations " + str(iterations))
        print(cmbGraph)

        print(cmbGraph.unmarked_list())
        if len(cmbGraph.unmarked_list()) == 0:
            # This means all combinations are marked
            return True
        else:
            return False


    @staticmethod
    def checkCopNumber2(g: Graph):
        # first define the lists of combinations

        cmbGraph = MultiComboGraph()

        for u in g.vList:
            for v in g.vList:
                for w in g.vList:
                    cmb1 = MultiCombination([u, v], w, True)
                    cmb2 = MultiCombination([u, v], w, False)
                    if u == w or v == w:
                        cmb1.marked = True
                        cmb2.marked = True

                    cmbGraph.add_vertex(cmb1)
                    cmbGraph.add_vertex(cmb2)

      
        # Add all the edges in the combo graph
        for cmb in cmbGraph.vList:
            if cmb.cop_turn:
                # Find all combinations where u has an edge to u'
                adjacent = [x for x in cmbGraph.vList if (not x.cop_turn and x.rober == cmb.rober and (x.check_cops_equal(cmb) or x.check_existing_adjascent_cops(cmb)))]

                for combo in adjacent:
                    cmb.add_edge(combo)
            else:
                # This is a rober turn
                adjacent = [x for x in cmbGraph.vList if x.cop_turn and x.check_cops_equal(cmb) and (x.rober == cmb.rober or x.rober.is_adjacent(cmb.rober))]

                for combo in adjacent:
                    cmb.add_edge(combo)

        print(cmbGraph)

        newMarked = True
        iterations = 0
        while newMarked:
            iterations += 1
            newMarked = False

            unmarkedCombos = cmbGraph.unmarked_list()

            for c in unmarkedCombos:
                if c.cop_turn:
                    #if there's a neighbour that's marked, mark this
                    markedNeighbor = next((x for x in c.adjacent if x.marked), None)
                    if markedNeighbor is not None:
                        c.marked = True
                        newMarked = True
                else:
                    # This is a rober turn
                    # if all neighbours are marked, mark this one. If there are no unmarked neighbours, they're all marked
                    unmarkedNeighbor = next((x for x in c.adjacent if not x.marked), None)

                    if unmarkedNeighbor is None:
                        c.marked = True
                        newMarked = True

        print("\n=============== AFTER MARKING =================")
        print("Iterations " + str(iterations))
        print(cmbGraph)

        print(cmbGraph.unmarked_list())
        if len(cmbGraph.unmarked_list()) == 0:
            # This means all combinations are marked
            return True
        else:
            return False

    @staticmethod
    def checkCopNumberN(g: Graph, n: int):
        # first define the lists of combinations
        comboList = list(itertools.product(g.get_key_list(), repeat=n+1))

        cmbGraph = MultiComboGraph()
        print("GENERATING COMBO GRAPH")
        for keyCombo in comboList:
            vrtList = [g.find_by_name(x) for x in keyCombo]
            cops = vrtList[:-1]
            rober = vrtList[-1]

            cmb1 = MultiCombination(cops, rober, True)
            cmb2 = MultiCombination(cops, rober, False)

            # If the rober is at the same position as any of the cops, mark these spots
            if rober in cops:
                cmb1.marked = True
                cmb2.marked = True

            cmbGraph.add_vertex(cmb1)
            cmbGraph.add_vertex(cmb2)

        print("ADDING EDGES")
        # Add all the edges in the combo graph
        for cmb in cmbGraph.vList:
            if cmb.cop_turn:
                # Find all combinations where u has an edge to u'
                adjacent = [x for x in cmbGraph.vList if (not x.cop_turn and x.rober == cmb.rober and cmbGraph.check_legal_cop_move(cmb, x))]

                for combo in adjacent:
                    cmb.add_edge(combo)
            else:
                # This is a rober turn
                adjacent = [x for x in cmbGraph.vList if x.cop_turn and x.check_cops_equal(cmb) and cmbGraph.check_legal_rober_move(cmb, x)]

                for combo in adjacent:
                    cmb.add_edge(combo)
            # print(cmb)
            # print("Added edges for combo " + cmb.name)

        # I think this is slower
        # for cmb in cmbGraph.vList:
        #     for x in cmbGraph.vList:
        #         if cmb.cop_turn:
        #             # Find all combinations where u has an edge to u'
        #             if (not x.cop_turn and x.rober == cmb.rober and (x.check_cops_equal(cmb) or x.check_existing_adjascent_cops(cmb))):
        #                 cmb.add_edge(x)

        #         else:
        #             # This is a rober turn
        #             if x.cop_turn and x.check_cops_equal(cmb) and (x.rober == cmb.rober or x.rober.is_adjacent(cmb.rober)):
        #                 cmb.add_edge(x)

        #     print("Added edges for combo " + cmb.name)

        # print(cmbGraph)

        newMarked = True
        iterations = 0
        while newMarked:
            print("MARKING, ITERATION " + str(iterations))
            iterations += 1
            newMarked = False

            unmarkedCombos = cmbGraph.unmarked_list()

            for c in unmarkedCombos:
                if c.cop_turn:
                    #if there's a neighbour that's marked, mark this
                    markedNeighbor = next((x for x in c.adjacent if x.marked), None)
                    if markedNeighbor is not None:
                        c.marked = True
                        newMarked = True
                else:
                    # This is a rober turn
                    # if all neighbours are marked, mark this one. If there are no unmarked neighbours, they're all marked
                    unmarkedNeighbor = next((x for x in c.adjacent if not x.marked), None)

                    if unmarkedNeighbor is None:
                        c.marked = True
                        newMarked = True

        print("\n=============== AFTER MARKING =================")
        print("Iterations " + str(iterations))
        # print(cmbGraph)

        print(cmbGraph.unmarked_list())
        if len(cmbGraph.unmarked_list()) == 0:
            # This means all combinations are marked
            return True
        else:
            return False
