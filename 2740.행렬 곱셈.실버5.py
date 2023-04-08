a,b= map(int, input().split())
l_li=[]
r_li=[]
total=[]
for _ in range(a):
    l_li.append(list(map(int, input().split())))

x,y = map(int, input().split())
for _ in range(x):
    r_li.append(list(map(int, input().split())))

for i in range(a):
    total.clear()
    for n in range(y):
        cnt=0
        for j in range(b):
            cnt+= l_li[i][j]*r_li[j][n]
        total.append(cnt)
    print(*total)
