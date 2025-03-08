n= int(input())
dp=[1]*n
arr=list(map(int,input().split()))
for i in range(n):
    for j in range(i):
        if arr[i]<arr[j]:
            dp[i]= max(dp[j]+1,dp[i])

print(max(dp))