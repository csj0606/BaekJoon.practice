"""
1. 아무나 괜찮은 사람 판별하고 조합
2. 3명의 서로 원하는 조합 구하기
3. 2명의 서로 원하는 조합 구하기 * 아무나 괜찮은 사람
4. 1+2+3 %10^9+7 구하기
"""

import sys
input = sys.stdin.readline

n= int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
graph = [[[],[]] for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][0].append(arr[i]) #포인터 값
    graph[arr[i]][1].append(i) #포인터 된 값
node1 = 0 
c1,c2,c3,c4,c5,c6,c7 = 0,0,0,0,0,0,0
for i in range(1,n+1):
    if i in graph[i][0] and i in graph[i][1]: #재귀노드 개수
        node1+=1
for i in range(1,n+1):
    if i in graph[i][0] and i in graph[i][1]:
        x = len(graph[i][1])
        if x>2:
            c1 += int((x*(x-1)/2)%(10**9+7)) # abc-> aaa 경우
        if x>1:
            c2 += int(((x-1)*(node1-1))%(10**9+7)) # abc-> abb 경우
    if i != arr[i]:
        if i == arr[arr[i]]:
            c3 += node1/2 #abc -> acb 경우
            c4 += (len(graph[i][1])-1)%(10**9+7) #abc-> bcb 경우
        if arr[arr[i]] == arr[arr[arr[i]]]:
            c5 += 1 #abc -> aab 경우
        if i == arr[arr[arr[i]]]:
            c6 += 1/3 #abc -> bca 경우
if node1>2:
    c7 = int((node1*(node1-1)*(node1-2)/6)%(10**9+7)) #abc-> abc 경우
print(int((c1+c2+c3+c4+c5+c6+c7))%(10**9+7))
