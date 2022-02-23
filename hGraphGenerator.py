import itertools
import sys
import json

import networkx as nx

k = 2

# NOTE: sys.argv[0] is the the name of the script
if len(sys.argv) > 1:
    k = int(sys.argv[1])

if k < 2:
    print("Must give a value of k >= 2")
else:
    graphName = "h" + str(k)
    prevGraph = "h" + str(k - 1)

    h1F = open('graphs/h1.json')
    hPrevF = open('graphs/' + prevGraph + '.json')
    
    # returns JSON object as a dictionary
    hPrevData = json.load(hPrevF)
    hPrevLines = [line + ' ' + ' '.join(hPrevData[line]) for line in hPrevData]
    hPrev = nx.parse_adjlist(hPrevLines)

    h1Data = json.load(h1F)
    h1Lines = [line + ' ' + ' '.join(h1Data[line]) for line in h1Data]
    h1 = nx.parse_adjlist(h1Lines, nodetype=str)


    print ("Calculating product")

    hk = nx.cartesian_product(hPrev, h1)

    hkData = {}
    # for line in nx.generate_adjlist(hk):
    for s, nbrs in hk.adjacency():
        key = s[0] + s[1]
        hkData[key] = []
        for t, data in nbrs.items():
            hkData[key].append(str(t[0] + t[1]))
        # key = line[0]
        # hkData[key] = line[1:].split(" ")

        # stripped = line.replace(", ", "").replace("'", "").strip("()").split(") (")
        # print(line)

    print(hkData)

    with open('graphs/' + graphName + '.json', 'w') as outfile:
        json.dump(hkData, outfile)
