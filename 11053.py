n=int(input())
li=list(map(int, input().split()))
lth=[0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if li[i] > li[j] and lth[i] < lth[j]:
            lth[i] = lth[j]
    lth[i] += 1
print(max(lth))