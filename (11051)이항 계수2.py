n,k =map(int,input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(k+1):
    dp[i][i] = 1
for x in range(1,n+1):
    for y in range(1,k+1):
        dp[x][y] = dp[x-1][y]+dp[x-1][y-1]
print((dp[-1][-1])%10007)