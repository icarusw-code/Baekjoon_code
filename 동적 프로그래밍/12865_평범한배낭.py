n, limit = map(int, input().split())

dp = [0] * (limit + 1)

for i in range(n):
    weight , value = map(int, input().split())
    for j in range(limit, weight -1 , -1):
        dp[j] = max(dp[j], dp[j-weight] + value) 

print(dp[limit])