n = int(input())
limit = 1000000
# 수열의 길이가 i 일때의 경우의 수
dp = [-1] * (limit + 1)

dp[1] = 1
dp[2] = 2

for i in range(3, limit + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
