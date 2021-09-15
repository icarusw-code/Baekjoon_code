n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

order = max(dp)
tmp = []

for i in range(n-1, -1, -1):
    if dp[i] == order:
        tmp.append(arr[i])
        order -= 1

print()

print(*tmp[::-1])