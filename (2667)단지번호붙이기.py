from collections import deque

n = int(input())
arr=[[]for _ in range(n)]
visited =[[0]*n for _ in range(n)]
num=[]

for i in range(n):
    tmp = int(input())
    for _ in range(n):
        arr[i].insert(0,tmp%10)
        tmp //= 10

def BFS(a,b):
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    cnt = 1
    visited[a][b]=1
    queue = deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and arr[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny]=1
                cnt += 1
    return(cnt)

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and visited[i][j] == 0:
            num.append(BFS(i,j))

num.sort()
print(len(num))
for item in num:
    print(item)