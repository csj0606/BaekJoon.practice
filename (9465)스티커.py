t = int(input())
for _ in range(t):
    n=int(input())
    dp=[]
    for _ in range(2):
        dp.append(list(map(int,input().split())))
    
    for i in range(n):
        if i==0:
            continue
        else:
            dp[1][i]+=dp[0][i-1]
            dp[0][i]+=dp[1][i-1]
    print(max(dp[0][n-1],dp[1][n-1]))