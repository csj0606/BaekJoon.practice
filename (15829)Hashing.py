import sys
input = sys.stdin.readline

# 입력
l = int(input())  # 문자열의 길이
lst = list(input().strip())  # 입력 문자열을 문자 리스트로 변환
h = 0

# 규칙 적용
for i, v in enumerate(lst):
    lst[i] = ord(v) - 96  # 각 문자를 숫자로 변환하여 리스트에 저장

# 해시 함수
for i, v in enumerate(lst):
    h += v * (31 ** i)  # 해시 값 계산

# 결과 출력
print(h%1234567891)  # 해시 값을 M으로 나눈 나머지 출력
input().strip