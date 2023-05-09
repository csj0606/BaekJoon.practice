import heapq , sys
heap=[]

n= int(input())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num !=0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)