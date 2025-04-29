from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))
que = deque(range(1, n + 1))
result = 0

for cur in target:
    while que[0] != cur:
        # 왼쪽으로 회전 (앞에서 꺼내려면)
        if que.index(cur) < len(que) / 2:
            que.rotate(-1)
        else:  # 오른쪽으로 회전
            que.rotate(1)
        result += 1
    que.popleft()  # 찾은 요소는 제거

print(result)
