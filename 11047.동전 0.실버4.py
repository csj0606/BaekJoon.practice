#greedy algorythm
n,k = map(int, input().split())

li=[0 for _ in range(n)]
for i in range(n):
    li[n-1-i] = int(input())

cnt=0
i=0
#가장 큰 단위 부터 나눌수 있을 만큼 나누어 그 몫을 저장,
#이후 다음 작은 수로 하강 계산
while k>0:
    if li[i]<=k:
        a,b= divmod(k, li[i])
        cnt+=a
        k=b
    i+=1
    
print(cnt)