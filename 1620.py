n,m = map(int, input().split())

_dict={}
for i in range(n):
    #dict 안에 번호:이름, 이름:번호로 포켓몬 저장
    name=input()
    _dict[i]=name
    _dict[name]=i+1

    #입력받은 이름or번호 키값에 해당하는 value값 출력
for _ in range(m):
    cnt = input()
    print(_dict[cnt])