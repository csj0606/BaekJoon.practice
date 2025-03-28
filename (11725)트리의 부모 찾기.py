from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

line = [[] for _ in range(n+1)]
for _ in range(n-1):
    a , b = map(int,input().split())
    line[a].append(b)
    line[b].append(a)

tree = [0]*(n+1)
visited = [False]*(n+1)
queue = deque()
queue.append(1)
while queue:
    cur = queue.popleft()
    visited[cur] = True
    for i in line[cur]:
        if visited[i] == False:
            tree[i] = cur
            queue.append(i)

for i in range(2,n+1):
    print(tree[i])