while True:
    arr = list(map(str,input())) #줄마다 문자열을 입력받음
    stack=[]
    if len(arr)==1 and arr[0]=='.': #온점 하나를 받으면 종료
        break
    for i in arr:
        if i =='.': #줄의 마지막 글자인 온점을 받았을 때 문자열이 균형을 이룬 상태인지 판단
            if len(stack)==0:
                print('yes')
                break
            else:
                print('no')
        if i == '(': #소괄호는 1로 스택에 삽입
            stack.append(1)
        if i =='[': #대괄호는 2로 스택에 삽입
            stack.append(2)
        if i == ')':
            if len(stack)==0 or stack[-1] != 1: #소괄호가 올바르게 닫혔는지 여부 판단
                print('no')
                break
            else:
                stack.pop(-1)
        if i ==']':
            if len(stack)==0 or stack[-1] !=2: #대괄호가 올바르게 닫혔는지 여부 판단
                print('no')
                break
            else:
                stack.pop(-1)