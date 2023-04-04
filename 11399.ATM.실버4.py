n=int(input())
li=list(map(int, input().split()))
total=0
li.sort(reverse=True)

for i in range(n):
    total+=li[i]*(i+1)

print(total)