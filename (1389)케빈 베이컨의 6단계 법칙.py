from collections import deque
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m): 
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(i):
    line=[0]*(n+1)
    visited=[0]*(n+1)
    queue = deque()
    queue.append(i)
    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = 1
                line[node] = line[x]+1
                queue.append(node)
    return sum(line)

best_kevin=1
for i in range(1,n+1):
    if BFS(best_kevin) > BFS(i):
        best_kevin = i
        
print(best_kevin)