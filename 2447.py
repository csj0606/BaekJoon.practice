def draw_stars(n):
    if n==1:
        return['*']
    L=[]
    stars = draw_stars(n/3)
    
    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star+' '*len(star)+star)
    for star in stars:
        L.append(star*3)
    
    return L

n = int(input())
print('\n'.join(draw_stars(n)))