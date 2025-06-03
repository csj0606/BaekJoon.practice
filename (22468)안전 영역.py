from collections import deque

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

max_height = max(max(row) for row in field)
max_safe_areas = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited, water_level):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and field[nx][ny] > water_level:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 모든 높이 수위에 대해 반복
for water_level in range(0, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    safe_area_count = 0

    for i in range(n):
        for j in range(n):
            if field[i][j] > water_level and not visited[i][j]:
                bfs(i, j, visited, water_level)
                safe_area_count += 1

    max_safe_areas = max(max_safe_areas, safe_area_count)

print(max_safe_areas)
