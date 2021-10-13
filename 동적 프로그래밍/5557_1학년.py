n = int(input()) - 1
arr = list(map(int, input().split()))
limit = 20
goal = arr[-1]
arr = arr[:-1]
dp = [[0] * (limit + 1) for _ in range(n)]

dp[0][arr[0]] = 1

for i in range(1, n):
    for j in range(limit + 1):
        if j - arr[i] >= 0:
            dp[i][j] += dp[i - 1][j - arr[i]]
        if j + arr[i] <= limit:
            dp[i][j] += dp[i - 1][j + arr[i]]

print(dp[n - 1][goal])
