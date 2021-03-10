
def floydWarshall(graph):
    n = len(graph)
    dist = [[] for i in range(n)]
        
    # Initialize the dist matrix as same as the input graph matrix.
    for i in range(n):
        for j in range(n):
            dist[i].append(graph[i][j])

    # k= Intermediate Vertices.
    # i = Source Vertices.
    # j =  Destinantion Vertices.
    for k in range(n):
        for i in range(n):
            for j in range(n):

                # Update the value of dist[i][j] if k provides a shortest path from i to j

                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

    return dist
