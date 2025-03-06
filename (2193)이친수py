"""

n자리 이친수
0끝 :0끝(n-1)자리+1끝(n-1)자리
1끝 :0끝(n-1)
"""
import sys
input = sys.stdin.readline()

n = int(input)
dp = [[0,0] for _ in range(n+1)]

for i in range(n+1):
    if i==1:
        dp[1][1]=1
    else:
        dp[i][0] = dp[i-1][0]+dp[i-1][1]
        dp[i][1] = dp[i-1][0]
print(dp[n][0]+dp[n][1])