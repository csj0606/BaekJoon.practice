while True:
    arr = list(map(str,input()))
    stack=[]
    if len(arr)==1 and arr[0]=='.':
        break
    for i in arr:
        if i =='.':
            if len(stack)==0:
                print('yes')
                break
            else:
                print('no')
        if i == '(':
            stack.append(1)
        if i =='[':
            stack.append(2)
        if i == ')':
            if len(stack)==0 or stack[-1] != 1:
                print('no')
                break
            else:
                stack.pop(-1)
        if i ==']':
            if len(stack)==0 or stack[-1] !=2:
                print('no')
                break
            else:
                stack.pop(-1)