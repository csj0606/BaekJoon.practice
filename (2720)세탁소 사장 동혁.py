T = int(input())
A = [25,10,5,1]
for _ in range(T):
    C = int(input())
    L = []
    for i in A:
        L.append(C//i)
        C %= i
    print(*L)