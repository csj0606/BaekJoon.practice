n = int(input())
dp=[0]*1000001
dp[0]=1
dp[1]=1
def func(n):
    if dp[n]:
        return dp[n]
    dp[n]=func(n-1)+func(n-2)
    return dp[n]
    
print(func(n)%15746)