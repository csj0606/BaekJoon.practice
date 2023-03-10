while True:
    n = int(input())
    if n ==-1:
        break

    sum=0
    slist =[]
    for i in range(1,n):
        if n % i ==0:
            sum+=i
            slist.append(str(i))
    
    if n == sum:
        print(n,'=',' + '.join(slist))
    else:
        print(n,'is NOT perfect.')