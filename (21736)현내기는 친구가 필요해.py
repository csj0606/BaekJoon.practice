#BFS
from collections import deque

n,m = map(int, input().split())
campus=[list(input()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(n):
    for j in range(m):
        if campus[i][j]=='I':
            queue = deque()
            queue.append((i,j))
            visited[i][j] = 1
def BFS():
    met = 0
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                info = campus[nx][ny]
                if info == 'O':
                    queue.append((nx,ny))
                elif info == 'P':
                    queue.append((nx,ny))
                    met += 1
    if met == 0:
        print('TT')
    else:
        print(met)
BFS()