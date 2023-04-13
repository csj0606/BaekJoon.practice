import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
bd=[0,n]
for i in range(m):
    t,r=map(int, input().split())
    bd[0]+=r
    if t<bd[1]:
        bd[1]=t
    if bd[0]>k:
        print(i+1,bd[1])
        break
if bd[0]<=k:
    print(-1)