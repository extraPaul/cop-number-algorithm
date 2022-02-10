import sys
import json

from project.copNumberChecker import CopNumberChecker
from project.graphTransformation import graphObjectFromJSON


# default graph is the square
graphName = "square"

# NOTE: sys.argv[0] is the the name of the script
if len(sys.argv) == 2:
    graphName = sys.argv[1]
 
# Opening JSON file
# f = open('graphs/triangleGraph.json')
# f = open('graphs/square.json')
# f = open('graphs/line.json')
# f = open('graphs/dodecahedron.json')

f = open('graphs/' + graphName + '.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

print(data)
print(data.keys())
print("===============================")
print()

graph = graphObjectFromJSON(data)

print(graph)

# Test cop number, starting at one and increassing.
num = 1
copWin = False

while not copWin:
    copWin = CopNumberChecker.checkCopNumberN(graph, num)

    if copWin:
        print("Cop number IS " + str(num))
    else:
        print("Cop number IS NOT " + str(num))
        num += 1