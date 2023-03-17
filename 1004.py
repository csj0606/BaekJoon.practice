def distance(a,b,x,y):
    return int((a-x)**2+(b-y)**2)


n = int(input())

for _ in range(n):
    x1,y1,x2,y2= map(int, input().split())
    cnt=0
    plenet=[]

    k=int(input())
    for _ in range(k):
        plenet.append(list(map(int, input().split())))
    
    for i in range(k):
        if distance(x1, y1, plenet[i][0], plenet[i][1])<(plenet[i][2])**2 <distance(x2, y2, plenet[i][0], plenet[i][1]) or distance(x1, y1, plenet[i][0], plenet[i][1])>(plenet[i][2])**2 >distance(x2, y2, plenet[i][0], plenet[i][1]):
            cnt+=1
    print(cnt)