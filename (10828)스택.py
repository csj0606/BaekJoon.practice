import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for _ in range(n):
    tmp = list(map(str,input().split()))
    if tmp[0]=='push':
        stack.append(int(tmp[1]))
    if tmp[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    if tmp[0]=='size':
        print(len(stack))
    if tmp[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    if tmp[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])