# O(n^4)의 시간복잡도를 가진다!!
# li=[]
# for _ in range(n):
#     li.append(list(str(input().rstrip())))
# min_rate=k*k
# for i in range(n-k+1):
#     for j in range(m-k+1):
#         cnt=0
#         for x in range(i,i+k):
#             for y in range(j,j+k):
#                 if (x+y)%2==0:
#                     if li[x][y]=='B':
#                         cnt+=1
#                 else:
#                     if li[x][y]=='W':
#                         cnt+=1
#         min_rate = min(cnt, k*k-cnt)
# print(min_rate)
import sys
input= sys.stdin.readline

n,m,k = map(int, input().split())
li=[]
bli=[[0 for _ in range(m+1)]for _ in range(n+1)]
wli=[[0 for _ in range(m+1)]for _ in range(n+1)]
for _ in range(n):
    li.append(list(input().rstrip()))

# O(N^2)
for i in range(1,n+1):
    for j in range(1,m+1):
        wli[i][j]=wli[i-1][j]+wli[i][j-1]-wli[i-1][j-1]
        bli[i][j]=bli[i-1][j]+bli[i][j-1]-bli[i-1][j-1]
        
        if (i+j)%2==0:
            if li[i-1][j-1]=='W':
                bli[i][j]+=1
            elif li[i-1][j-1]=='B':
                wli[i][j]+=1 
        else:
            if li[i-1][j-1]=='W':
                wli[i][j]+=1
            elif li[i-1][j-1]=='B':
                bli[i][j]+=1 

wmin=n*m
bmin=n*m
#O(N^2)
for i in range(n-k+1):
    for j in range(m-k+1):
        wmin=min(wmin, wli[i+k][j+k]-wli[i][j+k]-wli[i+k][j]+wli[i][j])
        bmin=min(bmin, bli[i+k][j+k]-bli[i][j+k]-bli[i+k][j]+bli[i][j])

print(min(wmin, bmin))
#O(N^4) -> O(N^2)으로 줄일수 있음