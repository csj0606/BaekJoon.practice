from collections import deque

n = int(input())
arr=[]
for i in range(n):
    arr.append(list(input()))

def NormalBFS():
    visited=[[0]*n for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                cnt+=1
                cur = arr[i][j]
                queue = deque()
                queue.append((i,j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==cur and visited[nx][ny]==0:
                            visited[nx][ny]=1
                            queue.append((nx,ny))
    return(cnt)

def colorblindBFS():
    cb_arr = arr.copy()
    for i in range(n):
        for j in range(n):
            if cb_arr[i][j]=='G':
                cb_arr[i][j]='R'
    visited=[[0]*n for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                cnt+=1
                cur = cb_arr[i][j]
                queue = deque()
                queue.append((i,j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<n and cb_arr[nx][ny]==cur and visited[nx][ny]==0:
                            visited[nx][ny]=1
                            queue.append((nx,ny))
    return(cnt)
print(NormalBFS(),colorblindBFS())