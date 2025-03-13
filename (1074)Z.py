N,r,c = map(int,input().split())
nst=0
r+=1
c+=1
while N!=0:
    plus=2**(2*(N-1))
    line=2**(N-1)
    if r<=line and c>line:
        c=c-line
        nst=nst+plus
    elif r>line and c<=line:
        r=r-line
        nst=nst+2*plus
    elif r>line and c>line:
        r=r-line
        c=c-line
        nst=nst+3*plus
    N-=1
print(nst)

