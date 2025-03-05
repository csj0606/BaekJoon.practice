import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,m+1): dp[1][i] = i


    for i in range(2,n+1):
        for j in range(1,m+1):
            for k in range(j, i-1, -1):
                dp[i][j] += dp[i-1][k-1]
    print(dp[n][m])
