n = int(input())
score = list(map(int, input().split()))

result = max(score) - min(score)

print(result)
