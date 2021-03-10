def bellman_ford(G,src):
    n = len(G)
    dist = [float("Inf")] * n
    dist[src] = 0
    predecessor=[None]*n

    # Step 2: relax edges |V| - 1 times
    for _ in range(n):
        for u, v, w in G:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v]=u
    # Step 3: detect negative cycle
    # if value changes then we have a negative cycle in the graph
    # and we cannot find the shortest distances
    for u, v, w in G:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    # No negative weight cycle found!
    # Print the distance and predecessor array
    return (dist,predecessor)