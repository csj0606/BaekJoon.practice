'''
1.탐색 정의
2.처음 온곳이면 탐색 실행
3.방문한 곳이면 결과가 이미 나온 곳이므로 그대로 반환
4.도달한 경우 1 반환
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_range(x, y, now):
    return 0 <= x < m and 0 <= y < n and arr[x][y] < now

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1  # 도달한 경우 1 반환
    if dp[x][y] == -1:
        dp[x][y] = 0  # 처음 방문한 곳이라면 0으로 초기화
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_range(nx, ny, arr[x][y]):  # 범위 내에 있고 현재 위치보다 작은 경우 상하좌우로 탐색
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))
