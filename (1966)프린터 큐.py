from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    number=0
    level = deque(list(map(int,input().split())))
    que = deque([i for i in range(n)])
    while True:
        if level[0]>=max(level):
            if que[0]==m:
                print(number+1)
                break
            else:
                level.popleft()
                que.popleft()
                number+=1
        else:
            a=level.popleft()
            b=que.popleft()
            level.append(a)
            que.append(b)