n=int(input())
road=list(map(int, input().split()))
value=list(map(int, input().split()))
total=value[0]*road[0]
cur_value=value[0]

for i in range(len(road)-1):
    cur_value=min(cur_value, value[i+1])
    total+=cur_value*road[i+1]

print(total)