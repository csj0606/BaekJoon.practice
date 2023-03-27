#n번째 계단을 밟기 위해서는
#1. n-2번째 계단에서 올라오거나
#2. n-2번째 계단을 밟지 않은 상태로 
#   n-1번째 계단에서 올라와야 한다
stairs=[0 for i in range(301)]
total=[0 for i in range(301)]

n=int(input())
for i in range(n):
    stairs[i]=int(input())
total[0]=stairs[0]
total[1]=stairs[0]+stairs[1]
total[2]=max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3,n):
    total[i]= max(stairs[i]+stairs[i-1]+total[i-3],stairs[i]+total[i-2])
print(total[n-1])