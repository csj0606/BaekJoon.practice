n=int(input())
dp=[x for x in range(n+1)]
for i in range(1,n+1):
    for j in range(i):
        if j*j>i:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i]=dp[i-j*j]+1
print(dp[-1])