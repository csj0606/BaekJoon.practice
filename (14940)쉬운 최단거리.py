n,m=map(int,input().split())
distance=[[0]*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]
maps=[]
ak,bk=0,0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    maps.append(list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,m+1):
        if maps[i-1][j-1]==2:
            ak=i
            bk=j
def BFS(x,y):
    visited[x-1][y-1]=1
    que=[[x,y]]
    while que:
        tmp = que.pop(0)
        for i in range(4):
            a = tmp[0]+dx[i]
            b = tmp[1]+dy[i]
            if 0<a<=n and 0<b<=m and visited[a-1][b-1]==0 and maps[a-1][b-1]==1:
                visited[a-1][b-1] = 1
                distance[a-1][b-1] = distance[tmp[0]-1][tmp[1]-1]+1
                que.append([a,b])
    for i in range(n):
        for j in range(m):
            if visited[i-1][j-1]==0:
                if maps[i-1][j-1]==1:
                    distance[i-1][j-1]=-1
    for i in distance:
        for j in i:
            print(j,end=" ")
        print()
BFS(ak,bk)