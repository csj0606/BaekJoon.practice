def Fac(n):
    cnt = 1
    for i in range(1,n+1):
        cnt *= i
    return cnt

n = int(input())
print(Fac(n))