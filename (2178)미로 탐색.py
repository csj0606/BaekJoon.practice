from collections import deque
n,m = map(int, input().split())

mage=[[] for _ in range(n)]
for i in range(n):
    k = int(input())
    for _ in range(m):
        mage[i].insert(0,int(k%10))
        k //= 10
visited = [[0]*(m) for _ in range(n)]
step = [[0]*(m) for _ in range(n)]

def BFS():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = [[0]*(m) for _ in range(n)]
    step = [[0]*(m) for _ in range(n)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and mage[nx][ny] == 1:
                visited[nx][ny] = 1
                step[nx][ny] = step[x][y] + 1
                queue.append((nx,ny))
    print(step[-1][-1]+1)

BFS()