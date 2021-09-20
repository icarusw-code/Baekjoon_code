T = int(input())

for _ in range(T):
    # 동전의 가지 수
    N = int(input())
    # 동전의 각 금액
    coin_value = list(map(int, input().split()))
    # 만들어야 할 금액
    M = int(input())

    # dp[i] i원 동전으로 j원 만드는 경우의 수
    dp = [0 for _ in range(M + 1)]
    dp[0] = 1

    for i in range(N):
        for j in range(coin_value[i], M +1):
            dp[j] += dp[j - coin_value[i]]

    print(dp[M])
    