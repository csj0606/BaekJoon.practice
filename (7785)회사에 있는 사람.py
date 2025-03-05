N = int(input())
people = set()
for _ in range(N):
    name, status = input().split()
    if status == 'enter':
        people.add(name)
    elif status == 'leave':
        people.remove(name)
for name in sorted(people, reverse=True):
    print(name)