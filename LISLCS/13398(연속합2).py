n = int(input())
arr = list(map(int, input().split()))

# 연속합
dp1 =[0] * n
dp2 =[0] * n
dp1[0] = arr[0]
dp2[0] = -1e9
result = -1e9

for i in range(1, n):
    dp1[i] = max(arr[i], dp1[i-1] + arr[i])
    dp2[i] = max(dp1[i -1], dp2[i-1] + arr[i])

for i in range(n):
    result = max(result, dp1[i], dp2[i])

print(result)