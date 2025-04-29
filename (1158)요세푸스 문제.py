# 입력 받기
n, k = map(int, input().split())

# 초기 연결 리스트 생성
linked_list = list(range(1, n + 1))
result = []

# 현재 위치 인덱스
current = 0

# 요세푸스 순열 계산
while linked_list:
    current = (current + k - 1) % len(linked_list)
    result.append(linked_list.pop(current))

# 결과 출력
print('<' + ', '.join(map(str, result)) + '>')
