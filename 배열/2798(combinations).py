from itertools import combinations

N, M = map(int, input().split())

card = list(map(int, input().split()))

com_card = list(combinations(card,3))
biggest_sum = 0

for i in com_card:
    temp_sum = sum(i)
    
    if biggest_sum < temp_sum <= M:
        biggest_sum = temp_sum
    
print(biggest_sum)
