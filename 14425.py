n,m = map(int, input().split())
cnt = 0
# dictionary 함수 선언할때는 {}중괄호 사용하기
_dict={}

for _ in range(n):
    _dict[input()] = 0

for _ in range(m):
    if input() in _dict:
        cnt += 1

print(cnt)