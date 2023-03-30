#누적합 알고리즘: n부터m까지 수열의 합을 구할 때 
# 시간복잡도를 보다 줄일 수 있는 방법 O(n**2) -> O(n)
from sys import stdin
input = stdin.readline


sumli=[]
n,m = map(int, input().split())
li=(list(map(int, input().split())))

sumli.append(li[0])
for i in range(1,n):
    sumli.append(li[i]+sumli[i-1])

for i in range(m):
    a,b=map(int, input().split())
    if a==1:
        print(sumli[b-1])
    else:
        print(sumli[b-1]-sumli[a-2])
