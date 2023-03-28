#a기준 정렬 -> b기준 lis구하기
n=int(input())
li=[]
lth=[0 for _ in range(n)]
for _ in range(n):
    li.append((list(map(int,input().split()))))

li.sort(key=lambda x:x[0])

lth[0]=1
for i in range(1,n):
    for j in range(i):
        if li[i][1]>li[j][1] and lth[i]<lth[j]:
         lth[i]=lth[j]
    lth[i]+=1

print(n-max(lth))