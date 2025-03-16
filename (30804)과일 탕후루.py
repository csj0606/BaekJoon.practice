#Sliding Window Algorythm 
#O(n**2) -> O(n)으로 줄임

n = int(input())
tanghuru = list(map(int,input().split()))

left = 0
fruit_count = {}
max_len = 0

for right in range(n):
    cur_fruit = tanghuru[right]

    if cur_fruit in fruit_count:    #현재 꼬치에 현재 과일이 있다면 +1, 없다면 과일 종류 추가
        fruit_count[cur_fruit] += 1
    else:
        fruit_count[cur_fruit] = 1

    while len(fruit_count) > 2:     #현재 꼬치의 과일 종류가 2개가 될 때까지 왼쪽 과일부터 제거
        remove_fruit = tanghuru[left]

        fruit_count[remove_fruit] -= 1

        if fruit_count[remove_fruit] == 0:
            del fruit_count[remove_fruit]
        
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)