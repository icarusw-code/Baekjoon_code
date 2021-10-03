import bisect
n = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
temp = [0] * n
b = []
for i in range(n):
    temp[a[i]-1] = i

for i in range(n):
    b.append(temp[c[i]-1])

dp = [b[0]]
for i in range(n):
    if b[i] > dp[-1]:
        dp.append(b[i])
    else:
        idx = bisect.bisect_left(dp, b[i])
        dp[idx] = b[i]
print(len(dp))