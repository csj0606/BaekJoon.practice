def dfs(start):
    if len(s)==m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

n,m=map(int, input().split())
s=[]

dfs(1)