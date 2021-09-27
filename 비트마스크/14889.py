# N명을 N/2명씩 두팀으로 나누려고한다. -> 팀이 2개이므로 비트마스크로 접근 가능
# 0번팀 1번팀 0 ~(1<<N) 까지 

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

answer = -1

#전체 for을 기준으로 데이터가 하나씩 내려감
for i in range((1<<n)):
    first = []
    second = []
    # 팀을 나누는 모든 경우를 탐색
    for j in range(n):
        # i가 j에 있는지 검사
        if (i & (1<<j)) > 0:
            first += [j]
        else:
            second += [j]

    # 팀이 2명씩 되어야 하므로 걸러줌
    if len(first) != n//2:
        continue
    
    t1 = 0
    t2 = 0
    for l1 in range(n//2):
        for l2 in range(n//2):
            if l1 == l2:
                continue

            t1 += s[first[l1]][first[l2]]
            t2 += s[second[l1]][second[l2]]
    
    diff = abs(t1- t2)
    if answer == -1 or answer > diff:
        answer = diff

print(answer)