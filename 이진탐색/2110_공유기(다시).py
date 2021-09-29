n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))

house = sorted(house)

min_gap = house[1] - house[0]
max_gap = house[-1] - house[0]
result = 0

while (min_gap <= max_gap):
    mid = (max_gap + min_gap) // 2 
    count = 1
    value = house[0]
    for i in range(1, n):
        if house[i] >= value + mid:
            value = house[i]
            count += 1
    if count >= c:
        result = mid 
        min_gap = mid + 1
    else:
        max_gap = mid - 1
print(result)
    