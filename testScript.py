import json
import itertools
from project.copNumberChecker import CopNumberChecker
from project.graphTransformation import graphObjectFromJSON


 
# Opening JSON file
# f = open('graphs/triangleGraph.json')
f = open('graphs/square.json')
# f = open('graphs/line.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

print(data)
print(data["B"])
print(data.keys())
print("===============================")
print()

graph = graphObjectFromJSON(data)

print(graph)

comboList = itertools.product(data.keys(), repeat=3) 

print(list(comboList))

# Test cop number
isNumber1 = CopNumberChecker.checkCopNumber1(graph)
isNumber1 = CopNumberChecker.checkCopNumberN(graph, 1)

if isNumber1:
    print("Cop numb IS 1")
else:
    print("Cop numb IS NOT 1")

    # isNumber2 = CopNumberChecker.checkCopNumber2(graph)
    isNumber2 = CopNumberChecker.checkCopNumberN(graph, 2)
    if isNumber2:
        print("Cop numb IS 2")
    else:
        print("Cop numb IS NOT 2")