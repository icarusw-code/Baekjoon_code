n = int(input())

arr = list(map(int, input().split()))

# arr[i] 를 마지막 원소로 가질 때 가장 긴 감소하는 부분수열 길이
min_len = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            min_len[i] = max(min_len[i], min_len[j] + 1)

print(max(min_len))