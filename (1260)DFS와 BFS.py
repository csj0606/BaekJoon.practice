from collections import deque
n,m,v = map(int,input().split())
graph=[[]for _ in range(n+1)]

for _ in range(m):
    a,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()

def BFS(v):
    visited=[0]*(n+1)
    queue= deque()
    queue.append(v)
    while queue:
        k = queue.popleft()
        if visited[k]==0:
            visited[k]=1
            print(k,end=' ')
            for i in graph[k]:
                queue.append(i)
    print()

def DFS(v):
    visited=[0]*(n+1)
    stack= deque()
    stack.append(v)
    while stack:
        k = stack.popleft()
        if visited[k]==0:
            visited[k]=1
            print(k,end=' ')
            for i in reversed(graph[k]):
                stack.insert(0,i)
    print()
DFS(v)
BFS(v)