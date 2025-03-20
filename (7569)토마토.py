from collections import deque
import sys
input = sys.stdin.readline
m,n,h=map(int,input().split())
box=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visited=[[[0]*m for _ in range(n)] for _ in range(h)]

queue= deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j]==1:
                queue.append((k,i,j))

def BFS():
    while queue:
        x,y,z = queue.popleft()
        dx = [-1, 1, 0, 0, 0, 0]
        dy = [0, 0, -1, 1, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                queue.append((nx,ny,nz))

BFS()
day=0
for layer in box:
    for row in layer:
        for i in row:
            if i==0:
                print(-1)
                exit()
            else:
                day = max(day,max(row))
print(day-1)