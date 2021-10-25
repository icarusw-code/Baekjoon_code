def go(lev, s):
    global max, min
    if lev == n + 1:
        if not len(min):
            min = s
        else:
            max = s
        return

    for i in range(10):
        if not used[i]:
            if lev == 0 or possible(s[-1], str(i), sign[lev - 1]):
                used[i] = 1
                go(lev + 1, s + str(i))
                used[i] = 0


def possible(i, j, k):
    if k == "<":
        return i < j
    if k == ">":
        return i > j
    return True


n = int(input())
sign = input().split()
used = [0] * 10
max, min = "", ""

go(0, "")
print(max)
print(min)
