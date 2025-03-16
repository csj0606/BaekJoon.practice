import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
arr=[]
for _ in range(n):
    arr.extend(map(int,input().split()))
time=[0]*257
maxhgt=0

for g in range(257):
    block = b
    for i in arr:
        if i<=g:
            time[g] += g - i
            block-= g - i                
        else:
            time[g] += 2 * (i - g)
            block += i-g
    if block >= 0 and time[g] <= time[maxhgt]:
        maxhgt = g

print(time[maxhgt],maxhgt)