n = int(input())
p = list(map(int, input().split()))


def min_time(n):
    p_sort = sorted(p)
    for i in range(1, n):
        p_sort[i] += p_sort[i-1]

    print(sum(p_sort))

min_time(n)        