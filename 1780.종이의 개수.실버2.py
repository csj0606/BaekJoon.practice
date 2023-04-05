n= int(input())
li=[list(map(int, input().split())) for _ in range(n)]
cnt=[0,0,0]
def novem_tree(a,b,n):
    pin = li[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if pin != li[i][j]:
                pin = 2
                break
    if pin==2:
        n=n//3
        novem_tree(a, b, n)
        novem_tree(a, b+n, n)
        novem_tree(a, b+2*n, n)
        novem_tree(a+n, b, n)
        novem_tree(a+n, b+n, n)
        novem_tree(a+n, b+2*n, n)
        novem_tree(a+2*n, b, n)
        novem_tree(a+2*n, b+n, n)
        novem_tree(a+2*n, b+2*n, n)
    elif pin==-1:
        cnt[0]+=1
    elif pin==0:
        cnt[1]+=1
    elif pin==1:
        cnt[2]+=1

novem_tree(0, 0, n)

for i in range(3):
    print(cnt[i])