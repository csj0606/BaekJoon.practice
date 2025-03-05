while True:
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    if a>=b+c or b>=c+a or c>=a+b:
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')    

'''
GPT의 간단화 코드
while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0:
        break
    if a + b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c:
        print('Isosceles')
    else:
        print('Scalene')
'''