'''
    BFS function takes a starting point S and Graph represented as Adjencey List
'''
def BFS(s,adj):
    level={s:0}
    parent= {s:None}
    i=1
    frontier=[s]
    while frontier:
        next=[]
        for u in frontier:
            for v in adj[u]:
                level[v]=i
                parent[v]=u
                next.append(v)
        i=i+1
        frontier=next


