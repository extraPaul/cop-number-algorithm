import sys
import json

import networkx as nx
import matplotlib.pyplot as plt


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

nx.draw(graph, with_labels = True)
plt.savefig('graphs/' + graphName + '.png')