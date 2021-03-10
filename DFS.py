"""
    Given a Graph represented as Adjencey List, Perform Depth first search
"""
def DFS(vertex,adj):
    parent={}
    for s in vertex:
        if s not in parent:
            parent[s] = None
            DFS_helper(s,adj,parent)

def DFS_helper(s,adj,parent):
    for v in adj[s]:
        parent[v]=s
        DFS_helper(v,adj,parent)


