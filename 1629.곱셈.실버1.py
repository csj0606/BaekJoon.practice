#시간복잡도를 O(logn)으로 만들기
a,b,c= map(int, input().split())

def div_mul(n,m,p):
    if m==1:
        return n%p
    if m%2==0:
        return (div_mul(n, m//2, p)**2)%p
    else:
        return ((div_mul(n, (m-1)//2, p)**2)*n%p)%p
print(div_mul(a, b, c))