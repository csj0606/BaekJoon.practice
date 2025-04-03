def backtracking(depth):
    check = 0
    if depth == m:
        print(*box)
        return
    for i in range(n):
        if check!= arr[i] and not visited[i]:
            visited[i] = 1
            box.append(arr[i])
            check = arr[i]
            backtracking(depth + 1)
            visited[i] = 0
            box.pop()

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))  # 정렬 추가
box = []
visited = [0] * n
backtracking(0)
