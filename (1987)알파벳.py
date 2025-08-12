import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited_states = set()
max_len = 1

def DFS(x, y, mask, cnt):
    global max_len
    max_len = max(max_len, cnt)

    if (x, y, mask) in visited_states:
        return
    visited_states.add((x, y, mask))

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            idx = ord(board[nx][ny]) - ord('A')
            if not (mask & (1 << idx)):
                DFS(nx, ny, mask | (1 << idx), cnt + 1)

start_mask = 1 << (ord(board[0][0]) - ord('A'))
DFS(0, 0, start_mask, 1)
print(max_len)
