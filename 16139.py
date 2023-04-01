import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [[0]*26]
arr[0][ord(s[0])-97] = 1
#[[0],[1],...,[0]]
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    #[[0,0],[1,1],...,[0,0]]
    arr[i][ord(s[i])-97] += 1
    #[[0,1],[1,1],...,[0,0]]
#결국 arr[n][m]은 문자열의 n번째 단어까지 
#세었을 때 m의 문자가 존재하는 개수의 합이다.

for _ in range(int(input())):
    c,start,end = list(input().split())
    start,end = map(int,[start,end])
    if start == 0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])