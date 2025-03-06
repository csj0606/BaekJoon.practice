"""
cardsum     0 1 2 3 4
num price   0 0 0 0 0
 1   1      0 1 2 3 4
 2   5      0 1 5 6 10 
 3   6      0 1 5 6 10
 4   7      0 1 5 6 10
 dp[k][p]= Max(price[p]+dp[k-p][p],dp[k][p-1])
"""

n = int(input())
cards = list(map(int,input().split()))
cards.insert(0,0)
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for y in range(1,n+1):
    for x in range(1,n+1):
        if y==1:
            dp[x][y]= cards[1]*x
        else:
            if x<y:
                dp[x][y]=dp[x][y-1]
            else:
                dp[x][y] = max(cards[y]+dp[x-y][y],dp[x][y-1])
print(dp[x][y])