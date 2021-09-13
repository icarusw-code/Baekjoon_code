# N M 자리의 비트 마스크
# A[i][j] = i x M + j
# 가로: 0 세로: 1 로 표현
n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
ans = 0
# 2차원 리스트를 1차원으로 표현 
for s in range(1<<(n*m)):
    sum = 0
    # 행 검사 (가로)
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m+j
            if (s&(1<<k)) == 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        # 세로 세로 가로 로 끝나는 경우 가로가 무시 될 수 있기때문에 더해줌
        sum += cur

        
    # 열 검사 (세로)
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            if (s&(1<<k)) != 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)
