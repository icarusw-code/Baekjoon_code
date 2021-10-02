word_1 = input()
word_2 = input()
word_3 = input()

n = len(word_1)
m = len(word_2)
k = len(word_3)

word_1 = ' ' + word_1
word_2 = ' ' + word_2
word_3 = ' ' + word_3

dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        for s in range(1, k+1):
            if word_1[i] == word_2[j] == word_3[s]:
                dp[i][j][s] = dp[i-1][j-1][s-1] + 1
            else: 
                dp[i][j][s] = max(dp[i][j][s-1], dp[i][j-1][s], dp[i-1][j][s])

print(dp[n][m][s])