def detectCycle(G): 
    color = { u : "white" for u in G  } 
    found_cycle = [False]
    for u in G:
        if color[u] == "white":
            dfs_visit(G, u, color, found_cycle)
        if found_cycle[0]:
            break
    return found_cycle[0]
 
def dfs_visit(G, u, color, found_cycle):
    if found_cycle[0]:               
        return
    color[u] = "grey"
    for v in G[u]:
        if color[v] == "grey":
            found_cycle[0] = True
            return
        if color[v] == "white":
            dfs_visit(G, v, color, found_cycle)
    color[u] = "black" 