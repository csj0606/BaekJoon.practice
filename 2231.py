n = int(input())

for i in range(1,n+1):
    a = list(map(int, str(i)))
    stn = i+sum(a)
    if stn==n:
        print(i)
        break
    if i==n:
        print(0)