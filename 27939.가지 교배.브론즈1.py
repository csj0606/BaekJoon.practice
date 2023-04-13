n= int(input())
color= list(input().split())
m,k=map(int, input().split())

for _ in range(m):
    is_w=True
    li=list(map(int, input().split()))
    for i in li:
        if color[i-1]=='P':
            is_w=False
            break
    if is_w:
        print('W')
        break
    else:
        continue
if is_w==False:
    print('P')
