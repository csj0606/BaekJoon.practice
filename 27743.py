def exp_mod(a,n,z):
    if n==1:
        return a
    if n%2==0:
        x= exp_mod(a, n/2, z)
        return (x*x)%z
    else:
        return (a*exp_mod(a, n-1, z))%z

n,m = map(int, input().split())
r = 10**9+7

if m==1:
    print((exp_mod(2, n, r)-1)%r)

else:
    print((((exp_mod(2, n, r)-1+r)%r)*((2*m)%r)%r-1+r) % r)