from DisjointSet import *

#Graph re
def kruskalMST(graph):
    vertices= graph.keys()
    mst=[]
    n= len(vertices)
    dis= DSU(n,vertices)
    for i,v in enumerate(dis.arr):
        dis.make_set(i,v)
    edgeList=[]
    for i in vertices:
        for j in graph[i].keys():
            edgeList.append((i,j,graph[i][j]))

    edgeList.sort(key=lambda x:x[2])
    for f, t, w in edgeList:
        a=dis.find_set(f)
        b=dis.find_set(t)
        if a==b:
            continue
        else:
            mst.append((f, t, w))
            dis.union_sets(f,t)
    return mst



