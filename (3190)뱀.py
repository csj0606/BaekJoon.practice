from collections import deque

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

# 입력 처리
n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]

# 사과 위치 입력
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1  # 1은 사과

# 방향 변환 정보
l = int(input())
turn_info = {}
for _ in range(l):
    x, c = input().split()
    turn_info[int(x)] = c

# 초기 상태
snake = deque()
snake.append((0, 0))
direction = 0  # 오른쪽
time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽 또는 자기 몸에 부딪힘
    if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in snake:
        break

    snake.append((nx, ny))

    # 사과가 있으면
    if board[nx][ny] == 1:
        board[nx][ny] = 0  # 사과 먹음
    else:
        snake.popleft()  # 꼬리 줄이기

    x, y = nx, ny

    # 방향 회전 체크
    if time in turn_info:
        direction = turn(direction, turn_info[time])

print(time)
