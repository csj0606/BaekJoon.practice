import collections
a=[]
b=[]

for _ in range(3):
    x,y=map(int, input().split())
    a.append(x)
    b.append(y)
print(min(a, key=a.count),min(b, key=b.count))
