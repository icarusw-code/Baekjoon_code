n = int(input())
count = n

for _ in range(n):
    word = input()
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        elif word[i] in word[i + 1 :]:
            count -= 1
            break
print(count)
