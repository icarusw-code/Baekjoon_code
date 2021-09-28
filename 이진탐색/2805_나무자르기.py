n, m = map(int, input().split())
tree_height = list(map(int, input().split()))
start, end = 1, max(tree_height)

while start <= end:
    mid = (start + end)//2

    sum = 0 # 벌목된 나무 총합
    for i in tree_height:
        if i >= mid:
            sum += i - mid

    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
