while True:
    n, limit = map(float, input().split())
    n = int(n)
    limit = int(limit*100 + 0.5)
    dp = [0] * (limit +1)

    if n==0 and limit ==0:
        break

    for i in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p*100 +0.5)
        for j in range(p, limit+1):
            dp[j] = max(dp[j], dp[j -p] + c)
    
    print(dp[limit])