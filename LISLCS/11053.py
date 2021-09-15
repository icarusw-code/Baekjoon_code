n = int(input())

arr = list(map(int, input().split()))

# arr[i] 를 마지막 원소로 가질 때 가장 긴 증가하는 부분수열 길이
max_len = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            max_len[i] = max(max_len[i], max_len[j] + 1)

print(max(max_len))