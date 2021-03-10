class DFSResult:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {} # Edge classification for directed graph.
        self.order = []
        self.t = 0

def dfs(g):
    results = DFSResult()
    for vertex in g.keys():
        if vertex not in results.parent:
            dfs_visit(g, vertex, results)
    return results
def dfs_visit(g, v, results, parent = None):
    results.parent[v] = parent
    results.t += 1
    results.start_time[v] = results.t
    if parent:
        results.edges[(parent, v)] = 'Tree Edge'

    for n in g[v].keys():
        if n not in results.parent: # n is not visited.
            dfs_visit(g, n, results, v)
        elif n not in results.finish_time:
            results.edges[(v, n)] = 'Back Edge'
        elif results.start_time[v] < results.start_time[n]:
            results.edges[(v, n)] = 'Forward Edge'
        else:
            results.edges[(v, n)] = 'Cross Edge'
    results.t += 1
    results.finish_time[v] = results.t
    results.order.append(v)