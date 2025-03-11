n=1
for _ in range(3):
    n*=int(input())
num=[0]*10
while n>=1:
    tmp = int(n%10)
    num[tmp]+=1
    n/=10
for i in num:
    print(i)