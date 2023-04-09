from collections import deque
import sys

while True:
    li=list(map(int, sys.stdin.readline().split()))
    n = li.pop(0)
    if n==0:
        break
    stack=deque()
    mxarea=0
    for i in range(n):
        while len(stack)!=0 and li[stack[-1]]>li[i]:
            tmp = stack.pop()

            if len(stack)==0:
                width = i
            else:
                width = i - stack[-1]-1
            mxarea = max(mxarea, width*li[tmp])
        stack.append(i)
    while len(stack)!=0:
        tmp = stack.pop()

        if len(stack)==0:
            width=n
        else:
            width = n-stack[-1]-1
        mxarea= max(mxarea, width*li[tmp])
    print(mxarea)