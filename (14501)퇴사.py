import sys
N = int(input())

schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dp = [0 for i in range(N+1)]
#Top_down
for i in range(N):
    for j in range(i+schedule[i][0], N+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

"""
Bottom_Up

for i in range(N-1,-1,-1):
    if schedule[i][0] > N-i:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],schedule[i][1]+dp[i+schedule[i][0]])
ptint(dp[0])
"""


print(dp[-1])

