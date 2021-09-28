target = input()
search = input()
count = 0
index = 0

while len(target) - index >= len(search):
    if target[index:index +len(search)] == search: # 찾고자하는 단어인 경우
        count += 1
        index += len(search)
    else:
        index += 1

print(count)
