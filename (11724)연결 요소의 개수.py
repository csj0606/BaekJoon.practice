import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m = map(int,input().split())
graph=[[]for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
cnt=0
for i in range(m):
    tmp=list(map(int,input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

def bfs(k):
    visited[k]=1
    for i in graph[k]:
        if not visited[i]:
            bfs(i)

for i in range(1,n+1):
    if visited[i]==0:
        bfs(i)
        cnt+=1
print(cnt)