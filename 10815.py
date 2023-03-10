

n = int(input())
ownC = list(map(int, input().split()))
m =int(input())
disC = list(map(int, input().split()))

_dict={}

for i in range(n):
    _dict[ownC[i]] = 0

for j in range(m):
    if disC[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')

