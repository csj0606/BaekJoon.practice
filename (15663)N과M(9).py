n , m = map(int,input().split())
arr = list(map(int,input().split()))

def backtracking(depth):
    if depth == m:
        cur = ''.join(map(str,box))
        if cur not in  result:
            result.append(cur)
        return 0
    for i in range(n):
        box.append(arr[i])
        backtracking(depth+1)
        box.del

box = []
result = []