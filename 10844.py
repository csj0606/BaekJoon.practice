#dp[자리의 번호][0~9의 값]=경우의수
dp=[[0 for i in range(10)]for i in range(100)]

dp[0][0]=0
for i in range(1,10):
    dp[0][i]=1

n=int(input())
for i in range(1,n):
    dp[i][0]=dp[i-1][1]%(10**9)
    dp[i][9]=dp[i-1][8]%(10**9)
    for j in range(1,9):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%(10**9)

print(sum(dp[n-1])%(10**9))