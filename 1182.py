def dfs(depth,s):
    global cnt,total
    if total==s and depth!=0:
        cnt+=1
    if depth==n:
        return
    for i in range(depth,n):
        total+=li[i]
        dfs(i+1,s)
        total-=li[i]

n,s = map(int, input().split())
li=list(map(int, input().split()))
cnt=0
total=0
dfs(0,s)
print(cnt)