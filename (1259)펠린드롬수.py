while 1:
    n= int(input())
    if n==0:
        break
    else:
        a=[]
        b=[]
        while n>=1:
            a.append(n%10)
            b.insert(0,n%10)
            n//=10
        if a==b:
            print('yes')
        else:
            print('no')