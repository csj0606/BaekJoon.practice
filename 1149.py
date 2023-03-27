from sys import stdin
input = stdin.readline
house=[]
n=int(input())
for _ in range(n):
    house.append(list(map(int, input().split())))
# i번째 집을 r색으로 칠하는 최솟값은 r로 칠하는 값+이전 집을 g또는b로 칠하는 최솟값

for i in range(1,n):
    house[i][0] += min(house[i-1][1],house[i-1][2])
    house[i][1] += min(house[i-1][2],house[i-1][0])
    house[i][2] += min(house[i-1][0],house[i-1][1])

print(min(house[n-1][0],house[n-1][1], house[n-1][2]))