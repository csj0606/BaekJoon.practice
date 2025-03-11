n,p = map(int,input().split())
dp = [[0 for _ in range(p+1)] for _ in range(n+1)]
dp[0][0]=1
for i in range(n+1):
    for j in range(1,p+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
print(dp[n][p]%1000000000)