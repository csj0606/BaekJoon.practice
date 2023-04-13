#lis algorythm을 이용하자.
#시간복잡도는 O(nlogn)이다.

n= int(input())
N=list(map(int, input().split()))
lis=[N[0]]

for item in N:
    if lis[-1] < item:
        lis.append(item)
    else:
        L=0
        R=len(lis)

        while L < R:
            mid = (L+R)//2
            if lis[mid] <item:
                L = mid+1
            else:
                R=mid
        lis[R]=item

print(len(lis))