# DP 가 어려워지면 중복없이 라는 조건이 생길 수 있는데 잘 알아두자

t = int(input())
limit = 10000
dp = [0] * (limit + 1)
dp[0] = 1

for i in range(1, limit + 1):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]


for i in range(1, limit + 1):
    if i - 2 >= 0:
        dp[i] += dp[i - 2]

for i in range(1, limit + 1):
    if i - 3 >= 0:
        dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])
