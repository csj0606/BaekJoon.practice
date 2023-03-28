# dp_upper[i] : i를 오름차순으로 탐색하여 i가 가장 큰 부분수열의 길이
# dp_lower[i] : i를 내림차순으로 탐색하여 i가 가장 큰 부분수열의 길이
# dp_bitonic[i] = dp_upper +dp_lower -1 : i를 기준으로 구한 바이토닉 수열의 최댓값

n=int(input())
dp_upper=[0 for _ in range(n)]
dp_lower=[0 for _ in range(n)]
dp_bitonic=[0 for _ in range(n)]
li=list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if li[i]>li[j] and dp_upper[i]<dp_upper[j]:
            dp_upper[i]=dp_upper[j]
    dp_upper[i]+=1
for i in range(n):
    for j in range(i):
        if li[-(i+1)]>li[-(j+1)] and dp_lower[-(i+1)]<dp_lower[-(j+1)]:
            dp_lower[-(i+1)]=dp_lower[-(j+1)]
    dp_lower[-(i+1)]+=1

for i in range(n):
    dp_bitonic[i]= dp_upper[i]+dp_lower[i]-1

print(max(dp_bitonic))
