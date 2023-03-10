def func(a,b):
    if b%a ==0:
        return 'factor'
    elif a%b==0:
        return 'multiple'
    else:
        return 'neither'


while True:
    a,b = map(int, input().split())
    if a==0 & b==0:
        break
    print(func(a, b))