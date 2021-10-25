# 일을 할 수도 있고 안할 수도 있다. -> o, x 두가지의 경우
# lev 의 범위가 정해져 있으므로 주어진 lev 값까지 경우를 구하면 된다.
# 값의 합을 구해야하므로 그 값을 담아줄 def go 에변수를 같이 선언한다.
# 최대값만 필요하므로 반환된 합의 값을 최신화 시켜주는게 더 시간이 적게 걸린다.


def go(lev, total):
    global answer
    if lev == n:
        # answer.append(total)
        if total > answer:
            answer = total
        return

    if lev > n:
        return
    # 선택한다.
    go(lev + arr[lev][0], total + arr[lev][1])
    # 선택 안한다.
    go(lev + 1, total)


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

result = 0

# answer = []
answer = 0
go(0, 0)
# print(max(answer))
print(answer)
