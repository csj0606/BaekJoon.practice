n,k= map(int, input().split())

for i in range(n):
    if n%(i+1)==0:
        k-=1
    if k==0:
        print(i+1)
        break
if k>0:
    print(0)