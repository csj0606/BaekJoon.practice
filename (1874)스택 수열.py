n=int(input())
num=[(i+1) for i in range(n)]
stack=[]
calcul=[]
for _ in range(n):
    cur_num=int(input())
    if len(stack)!=0:
            if cur_num==stack[-1]:
                stack.pop(-1)
                calcul.append('-')
            elif cur_num>stack[-1]:
                while cur_num>stack[-1]:
                    stack.append(num[0])
                    num.pop(0)
                    calcul.append('+')
                stack.pop(-1)
                calcul.append('-')
            else:
                calcul.clear()
                calcul.append('NO')
                break
    else:
        stack.append(num[0])
        num.pop(0)
        calcul.append('+')
        while cur_num>stack[-1]:
            stack.append(num[0])
            num.pop(0)
            calcul.append('+')
        stack.pop(-1)
        calcul.append('-')
         
for i in calcul:
    print(i)