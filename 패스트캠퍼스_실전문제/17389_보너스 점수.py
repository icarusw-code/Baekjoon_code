n = int(input())
answer = [0] + list(input())
score = 0
bonus = 0

for i in range(1, n + 1):
    if answer[i] == "O":
        score += i + bonus
        bonus += 1
    else:
        bonus = 0

print(score)
