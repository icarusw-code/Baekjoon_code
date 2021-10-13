# i번 곡을 볼륨 j로 연주 할 수 있는가 없는가 있으면 1 없으면 0

n, s, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]

dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == 0:
            continue
        if j - arr[i + 1] >= 0:
            dp[i + 1][j - arr[i + 1]] = 1
        if j + arr[i + 1] <= m:
            dp[i + 1][j + arr[i + 1]] = 1

ans = -1
for i in range(m + 1):
    if dp[n][i]:
        ans = i

print(ans)
