import sys
input = sys.stdin.readline
t = int(input())

def find_year(m,n,x,y):
    k = x
    while k <= m*n:
        if (k-x)%m == 0 and (k-y)%n == 0:
            return k
        k += m
    return -1

for _ in range(t):
    a,b,x,y = map(int,input().split())
    print(find_year(a,b,x,y))