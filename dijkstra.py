import heapq as hq
import math

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [None]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights