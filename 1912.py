import sys
input=sys.stdin.readline
#리스트를 2개 만드는게 핵심
n=int(input())
dp=list(map(int, input().split()))
total=[dp[0]]
for i in range(n-1):
    total.append(max(total[i]+dp[i+1],dp[i+1]))
print(max(total))
