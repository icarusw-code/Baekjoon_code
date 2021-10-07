import copy
from collections import deque

def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(x+1)
                board[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]
ans = 0

def bfs():
    global ans
    queue = deque()     
    w = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if w[i][j] == 2:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny < 0 or ny >= m:
                continue
            if w[nx][ny] == 0:
                w[nx][ny] = 2
                queue.append([nx,ny])
    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)


n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

wall(0)
print(ans)