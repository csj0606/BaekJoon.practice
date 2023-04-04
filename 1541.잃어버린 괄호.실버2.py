li=input().split('-')
wp=[]
for i in range(len(li)):
    wp.append(sum(map(int,li[i].split('+'))))

print(2*wp[0]-sum(wp))