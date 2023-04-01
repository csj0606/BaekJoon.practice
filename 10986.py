#N의 구간합을 M으로 나눈 나머지 구하기-> O(n)
#O(n^2)의 복잡도로 부분구간 생성-> 나머지 0이면 cnt+1
# import sys

# n,m=map(int, sys.stdin.readline().split())
# li=list(map(int, sys.stdin.readline().split()))

# res = [0 for _ in range(n)]
# res[0]=li[0]%m

# for i in range(1,n):
#     res[i] = (li[i]+res[i-1])%m


# for i in range(n):
#     for j in range(i,n):
#         if i==j and li[i]%m==0:
#             cnt+=1
#         else:
#             if (i==0 and res[j]%m==0) or (res[j]-res[i-1])%m==0:
#                 cnt+=1
#시간복잡도 너무 큼
import sys
 
n, m = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
 
remainder_info = [0 for _ in range(m)]
remainder_info[0] = 1
 
total = 0
for i in range(n):
    total += num_list[i]
    r = total % m
    # 나머지 값에 따라서 idx 정보 저장
    remainder_info[r] += 1
 
count = 0
for i in remainder_info:
    count += i*(i - 1) // 2
 
print(count)
