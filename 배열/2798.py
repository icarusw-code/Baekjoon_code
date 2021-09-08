N, M = map(int, input().split())

card = list(map(int, input().split()))
count = 0
result = 0

for i in range(len(card)):
    for j in range(i + 1, len(card)):
        for k in range(j + 1, len(card)):
            sum_value = card[i] + card[j] + card[k]
            if sum_value <= M:
                result = max(result, sum_value)

print(result)

