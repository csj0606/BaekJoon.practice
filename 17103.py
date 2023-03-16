# from sys import stdin

# #소수 판별
# def is_prime(a):
#     if a==0 or a==1:
#         return False
      
#     for i in range(2,int(a**(1/2))+1):
#         if a %i ==0:
#             return False
#     return True

# n = int(stdin.readline())

# for _ in range(n):
#     cnt = 0
#     num = int(stdin.readline())

#     #더해서 n인 두 수 a,b 가 모두 소수일 때 cnt +1
#     for a in range(1,int(num/2)+1):
#         if a%2==0:
#             continue
#         b = num-a
#         if is_prime(a) and is_prime(b):
#             cnt+=1
#     print(cnt)

import sys

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        #배수 모두 제거 -> 소수만 0으로 남김
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    print(count)