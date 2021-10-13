n = int(input())
arr = []
arr.append((0, 0, 0, 0))

for i in range(1, n + 1):
    area, height, weight = map(int, input().split())
    arr.append((i, area, height, weight))

# 무게 기준으로 정렬
arr.sort(key=lambda x: x[3])

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(0, i):
        # 너비가 넓을때만 값을 추가해준다
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + arr[i][2])

max_value = max(dp)
index = n
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(arr[index][0])
        max_value -= arr[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]
