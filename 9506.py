while True:
    n = int(input())
    if n ==-1:
        break

/// 약수를 구하는 경우, 에라토스테네스의 체를 이용한 방법으로 풀 수 있다. 

    sum=0
    slist=[]
    for i in range(2, n/2):
        if n % i ==0:
            sum+=i
            slist.append(str(i))

/// 본래대로 푼 방법           
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
