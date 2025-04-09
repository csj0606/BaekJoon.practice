n=int(input())
num=[(i+1) for i in range(n)] #숫자의 순서를 지키기 위한 배열 생성
stack=[]
calcul=[]

for _ in range(n):
    cur_num=int(input()) #현재 숫자를 입력받고
    if len(stack)!=0: #현재 스택에 숫자가 존재한다면 
            if cur_num==stack[-1]: #스택의 맨 위 숫자가 현재 숫자라면 -와 함께 POP 실행
                stack.pop(-1)
                calcul.append('-')

            elif cur_num>stack[-1]: #스택의 맨 위가 현재 숫자보다 작다면 
                while cur_num>stack[-1]: #스택의 맨 위 숫자가 현재 숫자와 같아질 때까지 +와 함께 PUSH 실행
                    stack.append(num[0])
                    num.pop(0)
                    calcul.append('+')
                stack.pop(-1) #이후 스택의 맨 위를 - 와 함께 POP 실행
                calcul.append('-') 
            else: #만약 스택의 맨 위가 현재 숫자보다 크다면 수열을 만들 수 없으므로 NO 출력
                calcul.clear()
                calcul.append('NO')
                break
    else: #현재 스택이 비어있다면
        stack.append(num[0]) #스택에 +와 함꼐 1를 추가
        num.pop(0)
        calcul.append('+')
        while cur_num>stack[-1]: #스택의 맨 위가 현재 숫자와 같아질 때 까지 숫자 PUSH 후 POP 실행
            stack.append(num[0])
            num.pop(0)
            calcul.append('+')
        stack.pop(-1)
        calcul.append('-')
         
for i in calcul:
    print(i) #수열을 만드는 동안 실행하였던 연산 출력