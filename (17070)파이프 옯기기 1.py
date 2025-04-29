from collections import deque
n = int(input())
graph = [[0]*n for _ in range(n)]
home = [list(map(int,input().split())) for _ in range(n)]
que = deque()
que.append([1,2,1])
while que:
    cur = que.popleft()
    if cur[0] == 1:
        if cur[1] == n:
            continue
        elif cur[2] == n:
            if home[cur[1]][cur[2]+1] == 0:
                graph[cur[1]][cur[2]+1] += graph[cur[1]][cur[2]]
                que.append([1,cur[1],cur[2]])
        else:
            graph[cur[1]][cur[2]+1] += graph[cur[1]][cur[2]]
            que.append([1,cur[1],cur[2]])
wile