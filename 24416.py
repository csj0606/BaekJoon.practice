def fib(n):
    global cnt1
    if n==1 or n==2:
        cnt1+=1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    global cnt2
    li[0]=1
    li[1]=1
    for i in range(2,n):
        cnt2+=1
        li[i] = li[i-1]+li[i-2]
        
n=int(input())

li=[0 for _ in range(n)]
cnt1=0
cnt2 =0
fib(n)
fibonacci(n)
print(cnt1, cnt2)