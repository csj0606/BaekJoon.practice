import sys

def gcd(a,b):
    while b!=0:
        n=a%b
        a=b
        b=n
    return a


intv=[]
n = int(sys.stdin.readline())
bf_num = int(sys.stdin.readline())

#가로수 간격 배열 생성
for i in range(n-1):
    num = int(sys.stdin.readline())
    intv.append(num-bf_num)
    bf_num = num

#최소 간격 도출 = 최대공약수
minrate = intv[0]
for i in range(1,len(intv)):
    minrate = gcd(minrate, intv[i])

cnt=0
for tv in intv:
    cnt += tv / minrate -1

print(int(cnt))

