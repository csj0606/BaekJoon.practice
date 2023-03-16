from sys import stdin

def is_prime(a):
    if a==0 or a==1:
        return False
      
    for i in range(2,int(a**(1/2))+1):
        if a %i ==0:
            return False
    return True

n = int(stdin.readline())

for i in range(n):
    num = int(stdin.readline())
    
    while True:
        if is_prime(num):
            print(num)
            break
        else:
            num+=1
            