n = int(input())
arr=list(map(int,input().split()))
t,p = map(int,input().split())
a=0
for i in range(6):
    a+= (arr[i]//t)
    if (arr[i]%t)!=0:
        a+=1
print(a)
print(n//p, n%p)