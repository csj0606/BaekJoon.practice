import sys
from collections import deque

n = int(input())
dec = deque()

def use_dec(q):
    if q[0] == '1': #1: 정수를 덱의 앞에 삽입 
        dec.appendleft(q[1])
    elif q[0] == '2': #2: 정수를 덱의 뒤에 삽입
        dec.append(q[1])
    elif q[0] == '3': #3. 덱에 정수가 있다면 맨앞의 정수 출력, 없으면 -1출력
        if dec:
            print(dec.popleft())
        else:
            print(-1)
    elif q[0] == '4': #4. 덱에 정수가 있다면 맨뒤의 정수 출력, 없으면 -1출력
        if dec:
            print(dec.pop())
        else:
            print(-1)
    elif q[0] == '5': #5. 덱의 정수 개수 출력
        print(len(dec))
    elif q[0] == '6': #6. 덱이 비어있는지 여부 출력
        if dec:
            print(0)
        else:
            print(1)
    elif q[0] == '7': #7. 덱에 정수가 있다면 맨앞의 정수 출력, 없다면 -1 출력
        if dec:
            print(dec[0])
        else:
            print(-1)
    elif q[0] == '8': #8. 덱에 정수가 있다면 맨뒤의 정수 출력, 없다면 -1 출력
        if dec:
            print(dec[len(dec)-1])
        else:
            print(-1)



for _ in range(n):
    q = sys.stdin.readline().split()
    use_dec(q)