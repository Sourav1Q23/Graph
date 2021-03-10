from collections import defaultdict
import heapq


def primMST(graph, source):
    mst = defaultdict(set)
    visited = set([source])
    ## Create an edges list if graph represent as a adjecncey list
    if isinstance(graph, dict):
        edges = [
            (source, to, cost)
            for to, cost in graph[source].items()
        ]
    ## Create an edges list if graph represent as adj matrix
    if isinstance(graph,list):    
        edges=[]
        for i in len(graph):
            for j in range(i+1,len(graph)):
                if graph[i][j] > 0:
                    edges.append(i,j, graph[i][j])

    heapq.heapify(edges)

    while edges:
        source, to, cost = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[source].add(to)
            for next, cost in graph[to].items():
                if next not in visited:
                    heapq.heappush(edges, (to, next, cost))

    return mst
