"""
1. 아무나 괜찮은 사람 판별하고 조합
2. 3명의 서로 원하는 조합 구하기
3. 2명의 서로 원하는 조합 구하기 * 아무나 괜찮은 사람
4. 1+2+3 %10^9+7 구하기
"""
import sys
input = sys.stdin.readline

n= int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
result = 0

selfnode = [[] for _ in range(n+1)]
secondnode = []
for i in range(1,n+1):
    if arr[i]==i:
        selfnode.append([i])
for i in range(1,n+1):
    if i!=arr[i] and len(selfnode[arr[i]])>0:
        selfnode[arr[i]].append(i)
for i in range(1,n+1):
    if i!=arr[i] and arr[arr[i]]==i and arr[i]>i:
        secondnode.append(i)
        secondnode.append(arr[i])
snc = 0
for i in range(len(selfnode)):
    snc += len(selfnode[i])
if snc>2:
    case1 = int(snc*(snc-1)*(snc-2)/6)
    result+=(case1)%(10**9+7)
if snc>1:
    case2=0
    for i in range(1,n+1):
        if len(selfnode[i])>1:
            case2+=(len(selfnode[i])-1)*snc
    result+=(case2)%(10**9+7)
if snc>0:
    case3,case4,case5=0,0,0
    for i in range(1,n+1):
        if len(selfnode[i])>2:
            tmp = len(selfnode[i])
            case3+= int(tmp*(tmp-1)/2)
        if len(selfnode[arr[i]])==0 and arr[i] in selfnode[arr[arr[i]]]:
            case5+=1
    if len(secondnode)>0:
        case4 = int((snc)*(len(secondnode)/2))
    result+=(case3+case4+case5)%(10**9+7)
if len(secondnode)>0:
    case7=0
    for i in range(1,n+1):
            if arr[i] in secondnode and i not in secondnode:
                case7+=1
    result+=(case7)%(10**9+7)
case6=0
for i in range(1,n+1):
    if i!=arr[i] and arr[arr[arr[i]]]==i:
        case6+=1
result+=(case6)%(10**9+7)
print((result)%(10**9+7))