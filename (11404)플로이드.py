import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 거리 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 노선이 여러 번 들어올 경우 최소값만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드–워셜
for k in range(1, n + 1):           # 경유지
    for i in range(1, n + 1):        # 출발지
        for j in range(1, n + 1):    # 도착지
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
