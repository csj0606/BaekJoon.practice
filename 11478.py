word = input()
index = set()

for i in range(len(word)):
    for j in range(i,len(word)):
        index.add(word[i:j+1])

print(len(index))