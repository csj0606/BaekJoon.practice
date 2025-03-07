import sys
input = sys.stdin.readline

n=int(input())
dp=[0]*n
arr=list(map(int,input().split()))
dp[0]=arr[0]
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+arr[i])
        else:
            dp[i]=max(dp[i],arr[i])

print(max(dp))

