def dfs(depth,index):
    global min_diff
    if depth == n//2:
        s_pow,l_pow =0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    s_pow += merge[i][j]
                elif not visited[i] and not visited[j]:
                    l_pow += merge[i][j]
        min_diff = min(min_diff, abs(s_pow-l_pow))
        return
    for i in range(index,n):
        if not visited[i]:
            visited[i]=True
            dfs(depth+1, i+1)
            visited[i]=False
    
n=int(input())
visited=[False for _ in range(n)]
merge=[list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)
