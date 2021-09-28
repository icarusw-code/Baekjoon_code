import sys
sys.setrecursionlimit(10000)

t = int(input())
# 가로, 세로, 개수
m, n, k = map(int, input().split())
cabbage =[[0]*m for _ in range(n)]

for _ in range(k):
    node1, node2 = map(int, input().split())
    cabbage[node2][node1] = 1

def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    
    if cabbage[x][y] == 1:
        cabbage[x][y] = 0 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(x,y)
        return True
    return False

count = 0
for _ in range(t):
    for i in range(n):
        for j in range(m):
            if cabbage(i,j) == True:
                dfs(i, j)
                count += 1
    print(count)