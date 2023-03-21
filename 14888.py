def cal(depth, total, plus, minus, multiply, divide):
    global maximum ,minimum
    if depth ==n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:
        cal(depth+1, total+num[depth], plus-1, minus, multiply, divide)
    if minus:
        cal(depth+1, total-num[depth], plus, minus-1, multiply, divide)
    if multiply:
        cal(depth+1, total*num[depth], plus, minus, multiply-1, divide)
    if divide:
        cal(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)

maximum = -1e914889.py

minimum = 1e9
n= int(input())
num=list(map(int, input().split()))
op=list(map(int, input().split()))

cal(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)