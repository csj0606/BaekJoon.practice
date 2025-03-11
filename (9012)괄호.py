n=int(input())
for _ in range(n):
    vps = list(map(str,input()))
    stack=0
    for i in vps:
        if i == '(':
            stack+=1
        if i == ')':
            stack-=1        
            if stack==0:
                break
    if stack==0:
        print('YES')
    else:
        print('NO')