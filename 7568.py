n = int(input())
WH=[]
score=[]
for _ in range(n):
    w,h = map(int, input().split())
    WH.append([w,h])

for i in range(n):
    #이눔의 k를 j for문 안에 넣어버려서 한참을 헤멤
    k=1
    for j in range(n):
        if (WH[i][0]<WH[j][0]) and (WH[i][1]<WH[j][1]):
            k+=1
    score.append(k)

print(*score)
