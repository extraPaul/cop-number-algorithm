from project.copNumberChecker import CopNumberChecker
from project.models.graph import Graph


def getGraphAdjacencyList(v, e):

    adjList = []

    for vrt in v:
        lst = filter(lambda x: vrt in x, e)
        adjLst = list(map(lambda x: x[1], lst))

        adjList.append((vrt, adjLst))


def graphObjectFromJSON(jsonObj):
    graph = Graph()

    # First create vertex ojects
    for key in jsonObj:
        print(key)
        print(jsonObj[key])

        graph.create_vertex(key)

    # Then add edges
    for vertex in graph.vList:
        strList = jsonObj[vertex.name]
        objList = [v for v in graph.vList if v.name in strList]
        for obj in objList:
            vertex.add_edge(obj)

    return graph
    

