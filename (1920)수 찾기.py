n = int(input())
arr1 = map(int, input().split())
arr1 = set(arr1)

m = int(input())
arr2 = map(int, input().split())

for num in arr2:
    if num in arr1:
        print('1')
    else:
        print('0')
        
#set 자료형을 사용하여 해쉬테이블 구현