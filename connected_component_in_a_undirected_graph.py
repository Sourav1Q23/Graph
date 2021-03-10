n, e = map(int,input().split())
graph=[[] for i in range(n)]
visited=[0]*n
connected=0
for i in range(e):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    visited[n]=1
    for i in graph[n]:
        if visited[i]==0:
            dfs(i)

for i in range(n):
    if visited[i]==0:
        dfs(i)
        connected+=1

print(connected)