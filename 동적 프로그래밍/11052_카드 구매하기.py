n = int(input())
card = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

dp[1] = card[1]
dp[2] = max(card[2], dp[1] + card[1])
dp[3] = max(card[3], dp[2] + card[1], dp[1] + card[2])
for i in range(5, n + 1):
    
