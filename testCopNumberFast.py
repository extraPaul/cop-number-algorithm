import sys
import json

from project.copNumberChecker import CopNumberChecker
from project.graphTransformation import graphKObjectFromJSON


# default graph is the square
graphName = "square"
activeGame = False

# NOTE: sys.argv[0] is the the name of the script
if len(sys.argv) > 1:
    graphName = sys.argv[1]

if len(sys.argv) > 2:
    activeGame = "-a" in sys.argv 
 
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

graph = graphKObjectFromJSON(data)

print(graph)

# Test cop number, starting at one and increassing.
num = 1
copWin = False

while not copWin:
    copWin = CopNumberChecker.checkCopNumberNFast(graph, num, activeGame)

    if copWin:
        print("Cop number IS " + str(num))
    else:
        print("Cop number IS NOT " + str(num))
        num += 1
