########핵심 아이디어#######
# 데이터의 개수가 굉장히 크며, 탐색을 해야 할때 -> 이진탐색을 고민해봐야 한다.
# 가장 인접한 두 공유기 사이의 최대 Gap 을 이진탐색으로 찾는다.

n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))
house.sort()
# house = [1 2 4 8 9]

min_gap = house[1] - house[0]
max_gap = house[-1] - house[0]
result = 0

while (min_gap <= max_gap):
    mid = (max_gap + min_gap) // 2
    value = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= value + mid:
            value = house[i]
            count += 1
    if count >= c:
        min_gap = mid + 1
        result = mid
    else:
        max_gap = mid -1 

print(result)