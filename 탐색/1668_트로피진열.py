def ascending(array):
    now = array[0]
    count = 1
    for i in range(1, len(array)):
        if now < array[i]:
            count += 1
            now = array[i]
    return count 

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

print(ascending(array))
array.reverse()
print(ascending(array))