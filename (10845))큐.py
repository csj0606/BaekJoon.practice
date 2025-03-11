import sys
input=sys.stdin.readline
n=int(input())
que=[]
for _ in range(n):
    tmp = list(map(str,input().split()))
    if tmp[0]=='push':
        que.append(int(tmp[1]))
    if tmp[0]=='pop':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
            que.pop(0)
    if tmp[0]=='size':
        print(len(que))
    if tmp[0]=='empty':
        if len(que)==0:
            print(1)
        else:
            print(0)
    if tmp[0]=='front':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    if tmp[0]=='back':
        if len(que)==0:
            print(-1)
        else:
            print(que[-1])