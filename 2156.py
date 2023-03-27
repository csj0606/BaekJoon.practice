li=[0 for _ in range(10000)]
mxdrink=[0 for _ in range(10000)]

n=int(input())
for i in range(n):
    li[i]=int(input())

mxdrink[0]=li[0]
mxdrink[1]=mxdrink[0]+li[1]
for i in range(2,n):
    mxdrink[i]=max(mxdrink[i-1],li[i]+li[i-1]+mxdrink[i-3], li[i]+mxdrink[i-2])

print(mxdrink[n-1])