import sys
input = sys.stdin.readline

n,k = int(input()), list(map(int,input().split()))
m,l = int(input()), list(map(int, input().split()))

dp= [[0 for _ in range(n*500+1)] for _ in range(n+1)]

def cal(num, weight):
    if num > n:
        return
    if dp[num][weight]:
        return
    
    dp[num][weight]=1

    cal(num+1,weight)
    cal(num+1, weight+k[num-1])
    cal(num+1, abs(weight-k[num-1]))

cal(0,0)
r=[]
for i in l:
    if i>15000:
        r.append("N")
        continue
    if dp[-1][i]==1:
        r.append("Y")
    else:
        r.append("N")
print(*r)