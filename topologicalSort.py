"""
Assume graph is represented as adjacency list
graph={
    'A':{'B':5,'C':6}
    'B':{'D:3}
    .
    .
    .
    .
}

"""

def topoSort(graph):
    n= len(graph.keys())
    visited={key:False for key in graph.keys()}
    order=[0]*n
    i=n-1

    for vertex in graph.keys():
        if visited[vertex] == False:
            i=dfs(i,vertex,visited,order,graph)
    return order   

def dfs(i,vertex,visited,order,graph):
    visited[vertex]=True
    for edge_to in graph[vertex].keys():
        if visited[edge_to] ==False:
            i= dfs(i,edge_to,visited,order,graph)
    order[i]=vertex
    return i-1
    