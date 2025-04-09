import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split()))) #q를 deque로 생성
ans = []

while q:
    idx, paper = q.popleft() #q의 가장 왼쪽 요소의 index, value POP
    ans.append(idx + 1) #answer 에 index+1 저장 (0부터 시작이므로)

    if paper > 0: #q의 value가 양수일 경우 1을 뺀 후 음수를 취해 rotate
        q.rotate(-(paper - 1))
    elif paper < 0: #q의 value가 음수일 경우 음수만을 취해 rotate
        q.rotate(-paper)

print(' '.join(map(str, ans))) #최종 answer를 출력