import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    op = sys.stdin.readline().split() #명령어를 입력받음
    if op[0] == '1':
        s.append(int(op[1])) #명령어 1 : 정수를 스택 s에 추가
    elif op[0] == '2':
        print(s.pop() if s else -1) #명령어 2 : 스택 s에서 정수를 제거, 없다면 -1 출력
    elif op[0] == '3':
        print(len(s)) #명령어 3 : 스택 s의 정수 개수 출력
    elif op[0] == '4':
        print(0 if s else 1) #명령어 4 : 스택이 비어있는지 여부를 판단해 0/1 출력
    elif op[0] == '5':
        print(s[-1] if s else -1) #명령어 5 : 스택의 맨 위 정수를 출력, 없다면 -1 출력
