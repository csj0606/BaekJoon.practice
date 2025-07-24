import sys
import heapq
input = sys.stdin.readline


# 입출력 ---------------------------------------------------
N, E = map(int, input().split())
edges = [[] for i in range(N+1)]

# 무방향 그래프이므로 하나의 간선에 대해 양쪽 노드 둘 다 정보 저장
for i in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
    
v1, v2 = map(int, input().split())


# 구현 ---------------------------------------------------
# 다익스트라 알고리즘(하나의 출발 노드로부터 모든 노드로의 최단 거리를
# 구하고, 그 중에서 목표 노드로의 최단 거리만 리턴)
def dijkstra(start, end):
    route = [sys.maxsize]*(N+1)
    route[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        cnt_w, cnt_node = heapq.heappop(q)
        
        if route[cnt_node] < cnt_w:
            continue
        
        for adjacency_node, adjacency_w in edges[cnt_node]:
            cal_w = route[cnt_node] + adjacency_w
            
            if cal_w < route[adjacency_node]:
                route[adjacency_node] = cal_w
                heapq.heappush(q, (cal_w, adjacency_node))
    
    return route[end]

# 최단 경로는 두 가지 가능한 경우의 수가 있다. (1 > v1 > v2 > N or 2 > v2 > v1 > N)
route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
route2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

# 만약 위 식에서 하나의 최단 거리라도 존재하지 않으면 그 경로의 값은 sys.maxsize가 된다.
# 이 경우를 조건문으로 걸러주어 상황에 맞는 올바른 답을 출력해준다.
if route1 >= sys.maxsize and route2 >= sys.maxsize:
    print(-1)
else:
    print(min(route1, route2))