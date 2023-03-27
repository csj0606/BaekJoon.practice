n = int(input())

li=[]

for i in range(n):
    li.append(list(map(int, input().split())))

if n==1:
    print(li[0][0])
else:
    for i in range(1,n):
        li[i][0] += li[i-1][0]
        li[i][-1]+= li[i-1][-1]
        if i>=2:
            for j in range(1,i):
                li[i][j] += max(li[i-1][j-1], li[i-1][j])

    print(max(li[-1]))