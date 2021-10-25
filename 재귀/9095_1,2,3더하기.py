# 가지치기 하였을때 한 숫자를 여러번 선택이 가능하다.
# lev 의 값이 정해지지 않았다


t = int(input())


def go(total):
    global answer
    if total > n:
        return
    if total == n:
        answer += 1
        return
    for i in range(1, 4):
        go(total + i)


for _ in range(t):
    n = int(input())
    answer = 0
    go(0)
    print(answer)
