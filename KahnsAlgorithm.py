"""
Graph is represneted as adjaceny list
graph={
    'A'=['B','C'],
    'B'=['C','E'],
    .
    .
    .
    .
}
"""


def kahnTopoSort(graph):
    in_degree = {u : 0 for u in graph}
    for vertices, neighbors in graph.items():
        in_degree.setdefault(vertices, 0)
        for neighbor in neighbors:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    q=[]
    for v in in_degree.keys():
        if in_degree[v]==0:
            q.append(v)

    order = []
    while q:
        vertex = q.pop()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    if len(order) != len(in_degree):
        print("Graph has cycles; It is not a directed acyclic graph ... ")
        return None
    else:
        return order