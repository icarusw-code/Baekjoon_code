n = int(input())

arr = list(map(int, input().split()))

result = [arr[0]]

for i in range(1, n):
    result.append((i + 1) * arr[i] - sum(result))

for i in result:
    print(i, end="")
