from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1): #가장 위 카드를 제거, 그 다음 위 카드를 맨 밑으로 이동을 반복
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])