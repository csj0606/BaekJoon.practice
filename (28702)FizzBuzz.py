def FzBz(a):
    if a%3 ==a%5 ==0:
        return('FizzBuzz')
    elif a%3 ==0:
        return('Fizz')
    elif a%5==0:
        return('Buzz')
    else:
        return a

for i in range(3,0,-1):
    a=input()
    if a!='Fizz' and a!='Buzz' and a!='FizzBuzz':
         x = int(a)+i
         print(FzBz(x))
         break