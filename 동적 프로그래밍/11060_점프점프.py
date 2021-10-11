n = int(input())
arr = list(map(int, input().split()))


# 위치까지 점프하는 최소 횟수
dp = [-1] * n
dp[0] = 0

for i in range(n):
    for j in range(i):
        if dp[j] != -1 and i - j <= arr[j]:
            dp[i] = min(dp[j]) + 1

print(dp)
