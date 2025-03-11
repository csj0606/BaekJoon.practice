arr = list(map(int,input().split()))
if arr[0]==1:
    for i in range(7):
        if arr[i]>arr[i+1]:
            print('mixed')
            break
        if i==6:
            print('ascending')
elif arr[0]==8:
    for i in range(7):
        if arr[i]<arr[i+1]:
            print('mixed')
            break
        if i==6:
            print('descending')
else:
    print('mixed')