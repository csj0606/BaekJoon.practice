from collections import deque
m,n=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
queue= deque()
for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            queue.append((i,j))

def BFS():
    while queue:
        x,y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            px=x+dx[i]
            py=y+dy[i]
            if 0<=px<n and 0<=py<m and box[px][py]==0:
                box[px][py] = box[x][y]+1
                queue.append((px,py))

BFS()
day=0
for row in box:
    for i in row:
        if i==0:
            print(-1)
            exit()
    else:
        day = max(day,max(row))
print(day-1)