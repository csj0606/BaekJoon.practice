import sys
input=sys.stdin.readline

save={}

n,m=map(int,input().split())
for _ in range(n):
    tmp = list(map(str,input().split()))
    save[tmp[0]]=tmp[1]
for _ in range(m):
    tmp = input().strip()
    print(save[tmp])
