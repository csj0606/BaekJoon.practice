import sys

n,m = map(int,sys.stdin.readline().split())
li=[[0 for _ in range(n+1)]]
for _ in range(n):
    li.append([0]+list(map(int,sys.stdin.readline().split())))

for i in range(1,n+1):
    for j in range(1,n+1):
        li[i][j]+=li[i-1][j]+li[i][j-1]-li[i-1][j-1]

for _ in range(m):
    a,b,c,d=map(int,sys.stdin.readline().split())
    print(li[c][d]-li[c][b-1]-li[a-1][d]+li[a-1][b-1])
