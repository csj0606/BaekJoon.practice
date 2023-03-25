n = int(input())
dp=[0]*1000001
dp[0]=1
dp[1]=1
def func(n):
    if n==1:
        return 1
    for i in range(2,n+1):
        dp[i]= (dp[i-1]+dp[i-2])%15746
    return dp[n]
        
print(func(n))
