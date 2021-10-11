def go(i, j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    ans = dp[i][j]
    cost = sum(arr[i : j + 1])
    for k in range(i, j):
        temp = go(i, k) + go(k + 1, j) + cost
        if ans == -1 or ans > temp:
            ans = temp
    dp[i][j] = ans
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[-1] * n for _ in range(n)]
    print(go(0, n - 1))
