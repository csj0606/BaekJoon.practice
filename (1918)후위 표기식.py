fm = input()
stack = []
answer = ''

for i in fm:
    if i == '(': #입력이 좌측 괄호일 경우 
        stack.append(i) #연산자 스택에 해당 괄호 삽입

    elif i == ')': #입력이 우측 괄호일 경우
        while stack and stack[-1] != '(': #좌측 괄호가 나올때까지 연산자를 POP하여 답에 입력
            answer += stack.pop()
        stack.pop() #이후 좌측 괄호 제거
    
    elif i == '*' or i == '/': #입력이 곱/나눔 연산자인 경우
        while stack and (stack[-1] == '*' or stack[-1] =='/'): 
            answer += stack.pop() #동위연산자가 스택에 존재하는 경우 해당 동위 연산자를 먼저 출력함.
        stack.append(i) #이후 동위연산자가 없다면 스택에 삽입 (하위연산자인 +,-가 존재하더라도 *, / 연산자가 우선순위를 가지기 때문)
    
    elif i == '+' or i == '-': #입력이 더하기/빼기 연산자일 경우
        while stack and stack[-1] != '(': #스택의 맨 위가 좌측 괄호이거나 스택이 빌 때까지
            answer += stack.pop() #스택의 연산자를 출력 (why? : 덧셈/뺄셈보다 하위의 연산자가 없기때문)
        stack.append(i) #이후 해당 연산자를 스택에 삽입
    
    else:
        answer += i #연산자가 아닐 경우 바로 답에 출력
    
while stack:
    answer += stack.pop() #마지막으로 스택에 남아있는 연산자를 순서대로 출력

print(answer)