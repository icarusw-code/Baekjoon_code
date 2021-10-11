n = int(input())

arr = []

for _ in range(n):
    input_data = input().split()
    arr.append((int(input_data[0]), input_data[1]))

ans = sorted(arr, key=lambda x: x[0])

for i in ans:
    print(i[0], i[1])
