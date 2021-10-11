word = input().lower()
check = list(set(word))
count = []

for i in check:
    cnt = word.count(i)
    count.append(cnt)

if count.count(max(count)) >= 2:
    print("?")
else:
    print(check[count.index(max(count))].upper())
