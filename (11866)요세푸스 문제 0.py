n,k = map(int,input().split())
cue = [(i+1) for i in range(n)]
cur=0
result=[]
for i in range(n,0,-1):
    cur = (cur+k)%(i)
    if cur == 0:
        cur = i
    result.append(cue[cur-1])
    cue.pop(cur-1)
    cur-=1

print('<',end='')
for i in range(n-1):
    print(result[i],end=', ')
print(result[n-1],end='')
print('>',end='')