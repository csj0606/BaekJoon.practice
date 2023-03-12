# import sys

# a,b = map(int, sys.stdin.readline().split())

# ali = list(map(int, sys.stdin.readline().split()))
# bli = list(map(int, sys.stdin.readline().split()))

# cnt=0
# if len(ali)<len(bli):
#     for i in range(len(ali)):
#         if ali[i] in bli:
#             cnt+=1
# else:
#     for i in range(len(bli)):
#         if bli[i] in ali:
#             cnt+=1
# print(len(ali)+len(bli)-2*cnt)

#위와 같은 주접을 떨 필요가 없다. 그냥 set함수를 사용하자.

from sys import stdin

n,m = map(int, stdin.readline().split())

ali=set(list(map(int, stdin.readline().split())))
bli=set(list(map(int, stdin.readline().split())))

print(len(ali-bli)+len(bli-ali))