import sys

n,m =map(int, sys.stdin.readline().split())
hp={}
cnt=0
hwp=[]

for _ in range(n):
    hp[input()]=0
for _ in range(m):
    wp = input()
    if wp in hp:
        cnt+=1
        hwp.append(wp)

hwp.sort()
print(cnt)
for i in range(len(hwp)):
    print(hwp[i])