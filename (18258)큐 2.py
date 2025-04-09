import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline())

for _ in range(N) :
    i = sys.stdin.readline().split()

    if i[0] == 'push' : #PUSH 연산
        queue.append(int(i[1]))
    
    elif i[0] == 'pop' : #POP 연산
        if not queue :
            print (-1)
        else :
            print(queue[0])
            queue.popleft()
    
    elif i[0] == 'size' : #SIZE 연산
        print(len(queue))
    
    elif i[0] == 'empty' : #EMPTY 연산
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    
    elif i[0] == 'front' : #FRONT 연산
        if not queue:
            print(-1)
        else :
            print(queue[0])
    
    elif i[0] == 'back' : #BACK 연산
        if not queue :
            print(-1)
        else :
            print(queue[-1])