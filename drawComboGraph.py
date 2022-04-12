import sys
import json

import graphviz
import networkx as nx
import matplotlib.pyplot as plt
from project.copNumberChecker import CopNumberChecker

from project.graphTransformation import graphObjectFromJSON
from project.models.graph import MultiComboGraph


def getGraphViz(graph: MultiComboGraph, name):
    g = graphviz.Digraph(name, format='png', engine="dot")

    with g.subgraph(name='cluster_0') as c:
        c.attr(color='invis')
        c.attr(label='Cop Turn')
        for n in graph.cop_list():
            # Name needs to be unique, but lable doesn't
            if False:
            # if n.marked:
                c.node(n.name, n.name.replace('-Cop', ''), style='filled')
            else:
                c.node(n.name, n.name.replace('-Cop', ''))
                

        # copList = sorted(graph.cop_list(), key=lambda x: x.name)
        # for i in range(len(copList) - 1):
        #     c.edge(copList[i].name, copList[i+1].name, style='invis')

        # c.attr(rankdir='TB')

    with g.subgraph(name='cluster_1') as c:
        c.attr(color='invis')
        c.attr(label='Robber Turn')
        for n in graph.robber_list():
            if False:
            # if n.marked:
                c.node(n.name, n.name.replace('-Rob', ''), style='filled')
            else:
                c.node(n.name, n.name.replace('-Rob', ''))

        # robberList = sorted(graph.robber_list(), key=lambda x: x.name)
        # for i in range(len(robberList) - 1):
        #     c.edge(robberList[i].name, robberList[i+1].name, style='invis')


    for e in graph.get_edges():
        g.edge(e[0], e[1])

    g.attr(rankdir='LR')
    g.attr(nodesep='1')
    g.attr(ranksep='4')

    return g


# default graph is the square
graphName = "square"

# NOTE: sys.argv[0] is the the name of the script
if len(sys.argv) > 1:
    graphName = sys.argv[1]
 
# Opening JSON file
f = open('graphs/' + graphName + '.json')
 
# returns JSON object as a dictionary
data = json.load(f)

graph = graphObjectFromJSON(data)
comboGraph = CopNumberChecker.generate_combo_graph(graph, 1, False)

# CopNumberChecker.markComboGraph(comboGraph)

vizGeraph = getGraphViz(comboGraph, graphName)
vizGeraph.render(directory='graphViz/combo')

# path = 'graphViz/' + graphName
# nx.write_graphml(graph, 'graphViz/')