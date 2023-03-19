s=[]
n,m = map(int, input().split())

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        s.append(i)
        if len(s)>1 and s[-1]<s[-2]:
            s.pop()
            continue
        dfs()
        s.pop()

dfs()