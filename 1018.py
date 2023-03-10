n,m = map(int, input().split())
d2li =[]

for _ in range(n):
    d2li.append(list(input()))


mnum=64
for i in range(n-7):
    for j in range(m-7):
        cnt=0
        for p in range(8):
            for q in range(8):
                if (i+j+p+q)%2==0 and d2li[i+p][j+q]=='W':
                    cnt+=1
                elif (i+j+p+q)%2==1 and d2li[i+p][j+q]=='B':
                    cnt+=1

        if min(cnt, 64-cnt) < mnum:
            mnum = min(cnt, 64-cnt)

print(mnum)