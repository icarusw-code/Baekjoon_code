import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < N) and (0 <= ny <M):
            if kimchi_cabbage[nx][ny] == 1:
                kimchi_cabbage[nx][ny] = -1
                dfs(nx, ny)        

for _ in range(t):
    #가로:M 세로:N
    M, N, K =map(int, input().split())
    kimchi_cabbage = [[0]*M for _ in range(N)]
    count = 0

    for _ in range(K):
        m,n = map(int, input().split())
        kimchi_cabbage[n][m] = 1

    for i in range(N):
        for j in range(M):
            if kimchi_cabbage[i][j]>0:
                dfs(i, j)
                count += 1

    print(count)