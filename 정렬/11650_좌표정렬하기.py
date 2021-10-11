n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

ans = sorted(arr)

for i in ans:
    print(i[0], i[1])
