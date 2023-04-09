n,m=map(int, input().split())
tree= list(map(int, input().split()))
start,end=1,max(tree)

while start<=end:
    mid = (start+end)//2
    cut=0
    for i in tree:
        if i > mid:
            cut+= i-mid
    if cut >=m:
        start=mid+1
    else:
        end=mid-1
print(end)