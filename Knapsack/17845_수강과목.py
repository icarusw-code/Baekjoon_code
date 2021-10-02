max_time, k = map(int, input().split())

dp = [0] * (max_time +1)

for i in range(k):
    value, importance = map(int, input().split())
    for j in range(max_time, importance-1, -1):
        dp[j] = max(dp[j], dp[j - importance] + value)

print(max(dp))