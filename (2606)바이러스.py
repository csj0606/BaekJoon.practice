n=int(input())
m=int(input())
computer=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)
visited=[0]*(n+1)
visited[1]=1
q=[1]
while q:
    x=q.pop(0)
    for i in computer[x]:
        if not visited[i]:
            visited[i]=1
            q.append(i)
print(visited.count(1)-1)