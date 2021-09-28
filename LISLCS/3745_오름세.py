from bisect import bisect_left
# EOF 예외처리
while True:
    try:
        n = int(input())
        array = list(map(int, input().split()))

        dp = [array[0]]

        for i in range(1, n):
            if array[i] > dp[-1]:
                dp.append(array[i])
            else:
                dp[bisect_left(dp, array[i])] = array[i]

        print(len(dp))

    except EOFError:
        break

