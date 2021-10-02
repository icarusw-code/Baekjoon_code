## 답이 안나옴
t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    n_1 = arr[0]
    n_2 = arr[3]

    list_1 = [arr[1]]
    for i in range(n_1):
        list_1.append(list_1[-1] + arr[2])
    
    list_2 = [arr[4]]
    for i in range(n_2):
        list_2.append(list_2[-1]+ arr[5])

    list_1 = [' '] + list_1
    list_2 = [' '] + list_2

    dp = [[0] * (n_2+1) for _ in range(n_1+1)]

    for i in range(1, n_1 + 1):
        for j in range(1, n_2 + 1):
            if list_1[i] == list_2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i],[j-1])
    
    print(dp[n_1][n_2])