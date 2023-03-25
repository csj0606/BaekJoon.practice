from sys import stdin

dp=[0]*100
dp[0]=dp[1]=dp[2]=1
dp[3]=dp[4]=2

for n in range(5,100):
    dp[n]=dp[n-1]+dp[n-5]

k=int(stdin.readline())
for _ in range(k):
    print(dp[int(stdin.readline())-1])
