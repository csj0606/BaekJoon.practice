n=int(input())
stack=[]
for i in range(n):
    tmp = int(input())
    if tmp == 0:
        stack.pop(-1)
    else:
        stack.append(tmp)
sm=0
for i in stack:
    sm+=i
print(sm)