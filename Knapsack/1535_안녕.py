n = int(input())
attack = list(map(int, input().split()))
value = list(map(int, input().split()))

hp = 99
dp = [0] * (hp+1)

for i in range(n):
    for j in range(hp, attack[i]-1, -1):
        dp[j] = max(dp[j], dp[j-attack[i]]+ value[i])

print(max(dp))