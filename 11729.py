def move_pannel(n,a,b):
    if n==1:
        print(a,b)
    elif n>1:
        for i in range(1,4):
            if i !=a and i!=b:
                move_pannel(n-1, a, i)
                print(a,b)
                move_pannel(n-1, i, b)

n =int(input())
print(2**n-1)
move_pannel(n, 1, 3)