import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == '1':
        s.append(int(op[1]))
    elif op[0] == '2':
        print(s.pop() if s else -1)
    elif op[0] == '3':
        print(len(s))
    elif op[0] == '4':
        print(0 if s else 1)
    elif op[0] == '5':
        print(s[-1] if s else -1)
