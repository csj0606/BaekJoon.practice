n,m = map(int, input().split())

li= list(map(int, input().split()))
mxsum=0

for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1, len(li)):
            if mxsum <li[i]+li[j]+li[k] <= m:
                mxsum = li[i]+li[j]+li[k]

print(mxsum)