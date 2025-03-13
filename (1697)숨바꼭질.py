n,k = map(int,input().split())
visited=[0]*100001
MAX = 10**5
def bfs(a):
    que=[a]
    while que:
        tmp=que[0]
        que.pop(0)
        if tmp == k:
            return visited[tmp]
        for i in (tmp-1,tmp+1,tmp*2):
            if 0<=i<=MAX and not visited[i]:
                visited[i] = visited[tmp]+1
                que.append(i)
#BFS를 사용, 최소시간은 Depth가 낮을때 구해지므로 한번 구해진 노드를 다시 탐색할 필요가 없다!!!
print(bfs(n))