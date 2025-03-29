a,b = map(int,input().split())

r=1
while(b!=a):
    r+=1
    tmp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if tmp == b:
        print(-1)
        break
else:
    print(r)