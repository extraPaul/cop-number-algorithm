import sys
import json

import graphviz
import networkx as nx
import matplotlib.pyplot as plt


def getGraphViz(graph: nx.Graph, name):
    viz = graphviz.Graph(name, format='png', engine='dot')

    for n in list(graph.nodes):
        viz.node(n)

    for e in list(graph.edges):
        viz.edge(e[0], e[1])

    # viz.attr(rankdir='LR')

    return viz


# default graph is the square
graphName = "square"

# NOTE: sys.argv[0] is the the name of the script
if len(sys.argv) > 1:
    graphName = sys.argv[1]
 
# Opening JSON file
f = open('graphs/' + graphName + '.json')
 
# returns JSON object as a dictionary
data = json.load(f)

lines = [line + ' ' + ' '.join(data[line]) for line in data]

graph = nx.parse_adjlist(lines, nodetype=str)

# OLD WAY OF DRAWING
# nx.draw(graph, with_labels = True, node_color="#ffffff")
# nx.draw(graph, with_labels = True)
# plt.savefig('graphs/' + graphName + '.png')

vizGeraph = getGraphViz(graph, graphName)
vizGeraph.render(directory='graphViz')

# path = 'graphViz/' + graphName
# nx.write_graphml(graph, 'graphViz/')